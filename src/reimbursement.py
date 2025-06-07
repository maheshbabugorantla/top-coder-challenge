import math
import json
import os
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Import ML libraries for loading only
try:
    import joblib
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

# Model persistence paths
MODEL_DIR = 'models'
MODEL_PATH = os.path.join(MODEL_DIR, 'best_reimbursement_model.pkl')
MODEL_INFO_PATH = os.path.join(MODEL_DIR, 'model_info.json')

def create_features_simple(duration, miles, receipts):
    """Create simple feature set matching train_and_export.py format"""
    if duration <= 0:
        return None

    miles_per_day = miles / duration
    spend_per_day = receipts / duration

    # Simple feature engineering from train_and_export.py - return as list for m2cgen compatibility
    features = [
        duration,                           # trip_duration_days
        miles,                             # miles_traveled
        receipts,                          # total_receipts_amount
        miles_per_day,                     # miles_per_day
        spend_per_day,                     # spend_per_day
        int(miles // 50),                  # miles_bucket
        int(receipts // 50),               # receipts_bucket
        int(miles_per_day // 25),          # miles_per_day_bucket
        int(spend_per_day // 25),          # spend_per_day_bucket
    ]

    return features

def load_saved_model():
    """Load the saved model for inference only"""
    if not os.path.exists(MODEL_PATH) or not os.path.exists(MODEL_INFO_PATH):
        return None, None

    try:
        # Load the model
        model = joblib.load(MODEL_PATH)

        # Load model metadata
        with open(MODEL_INFO_PATH, 'r') as f:
            model_info = json.load(f)

        return model, model_info['score']
    except Exception as e:
        print(f"Error loading saved model: {e}")
        return None, None

# Global model variables for caching
_model = None
_model_score = None
_model_loaded = False

def get_model():
    """Get the loaded model (load once, use many times)"""
    global _model, _model_score, _model_loaded

    if _model_loaded:
        return _model, _model_score

    if not SKLEARN_AVAILABLE:
        _model_loaded = True
        return None, None

    # Load the saved model
    _model, _model_score = load_saved_model()
    _model_loaded = True

    # if _model is not None:
    #     print(f"Loaded trained model with CV MAE: {_model_score:.2f}")
    # else:
    #     print("No trained model found. Please run model training first.")

    return _model, _model_score

def calculate_reimbursement_ml(trip_details):
    """ML-based reimbursement calculation using saved model"""
    duration = trip_details['trip_duration_days']
    miles = trip_details['miles_traveled']
    receipts = trip_details['total_receipts_amount']

    if duration <= 0:
        return 0.0

    model, score = get_model()
    if model is None:
        return calculate_reimbursement_fallback(trip_details)

    features = create_features_simple(duration, miles, receipts)
    if features is None:
        return calculate_reimbursement_fallback(trip_details)

    prediction = model.predict([features])[0]
    return round(max(0, prediction), 2)


def calculate_reimbursement_fallback(trip_details):
    """Fallback to Lisa's rule-based model if ML model not available"""
    duration = trip_details['trip_duration_days']
    miles = trip_details['miles_traveled']
    receipts = trip_details['total_receipts_amount']

    if duration <= 0:
        return 0.0

    # Lisa's rule-based model
    base_per_diem = duration * 100.0
    if duration == 5:
        base_per_diem *= 1.1

    if miles <= 100:
        mileage_reimbursement = miles * 0.58
    else:
        mileage_reimbursement = 100 * 0.58 + (miles - 100) * 0.45

    if receipts <= 50 and duration > 1:
        receipt_reimbursement = 0
    elif receipts <= 1000:
        receipt_reimbursement = receipts * 0.80
    elif receipts <= 1200:
        receipt_reimbursement = 800 + (receipts - 1000) * 0.25
    else:
        receipt_reimbursement = 850 + (receipts - 1200) * 0.1

    total_reimbursement = base_per_diem + mileage_reimbursement + receipt_reimbursement

    spending_per_day = receipts / duration if duration > 0 else 0
    if duration > 10 and spending_per_day > 200:
        total_reimbursement *= 0.9

    cents = receipts - int(receipts)
    if math.isclose(cents, 0.49, abs_tol=0.001) or math.isclose(cents, 0.99, abs_tol=0.001):
        total_reimbursement += 5.0

    return round(total_reimbursement, 2)


def calculate_reimbursement(trip_details):
    """Main calculation function - tries m2cgen export first, then ML model, then fallback"""
    # Try to use the m2cgen exported model first (fastest)
    try:
        from src.reimbursement_model_v2 import score

        # parse inputs
        trip_duration_days = float(trip_details['trip_duration_days'])
        miles_traveled = float(trip_details['miles_traveled'])
        receipts_amount = float(trip_details['total_receipts_amount'])

        # compute derived features matching train_and_export.py format
        miles_per_day = miles_traveled / trip_duration_days
        spend_per_day = receipts_amount / trip_duration_days

        features = [
            trip_duration_days,            # trip_duration_days
            miles_traveled,               # miles_traveled
            receipts_amount,              # total_receipts_amount
            miles_per_day,                # miles_per_day
            spend_per_day,                # spend_per_day
            int(miles_traveled // 50),    # miles_bucket
            int(receipts_amount // 50),   # receipts_bucket
            int(miles_per_day // 25),     # miles_per_day_bucket
            int(spend_per_day // 25),     # spend_per_day_bucket
        ]

        return round(score(features), 2)
    except ImportError:
        # Fall back to loading the pickled model
        return calculate_reimbursement_fallback(trip_details)
