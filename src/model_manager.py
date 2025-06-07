#!/usr/bin/env python3

import sys
import argparse
import json
import os
import warnings
from pathlib import Path
import re # For ImportError parsing

warnings.filterwarnings('ignore')

# Placeholder for modules to be imported in main()
np = None
pd = None
m2c = None
XGBRegressor = None
RandomForestRegressor = None
KFold = None
GridSearchCV = None
cross_val_score = None
train_test_split = None
mean_squared_error = None
mean_absolute_error = None
joblib = None

# Model persistence paths
MODEL_DIR = 'models'
MODEL_PATH = os.path.join(MODEL_DIR, 'best_reimbursement_model.pkl')
MODEL_INFO_PATH = os.path.join(MODEL_DIR, 'model_info.json')
M2CGEN_OUTPUT_DIR = 'src'
M2CGEN_MODEL_PATH = os.path.join(M2CGEN_OUTPUT_DIR, 'reimbursement_model.py')

def ensure_dir(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

ensure_model_dir = lambda: ensure_dir(MODEL_DIR)
ensure_m2cgen_output_dir = lambda: ensure_dir(M2CGEN_OUTPUT_DIR)


def create_features_simple(duration, miles, receipts):
    if duration <= 0:
        return None
    miles_per_day = miles / duration
    spend_per_day = receipts / duration
    features = {
        'trip_duration_days': float(duration),
        'miles_traveled': float(miles),
        'total_receipts_amount': float(receipts),
        'miles_per_day': float(miles_per_day),
        'spend_per_day': float(spend_per_day),
        'miles_bucket': int(miles // 50),
        'receipts_bucket': int(receipts // 50),
        'miles_per_day_bucket': int(miles_per_day // 25),
        'receipt_cents': int(round((receipts * 100)) % 100),
        'spend_per_day_bucket': int(spend_per_day // 25),
    }
    return features


def load_training_data():
    global pd, np
    if pd is None or np is None:
        print("Critical Error: Pandas or NumPy modules not loaded before calling load_training_data.")
        sys.exit(1)
    try:
        data_paths = ['public_cases.json', '../public_cases.json']
        cases = None
        for path in data_paths:
            try:
                with open(path, 'r') as f: cases = json.load(f)
                print(f"Loaded training data from {path}")
                break
            except FileNotFoundError: continue
        if cases is None:
            print("Could not find public_cases.json.")
            return None, None
        records, y_targets = [], []
        for case in cases:
            input_data = case.get('input', {})
            duration = input_data.get('trip_duration_days')
            miles = input_data.get('miles_traveled')
            receipts = input_data.get('total_receipts_amount')
            expected_output = case.get('expected_output')

            if duration is None or miles is None or receipts is None or expected_output is None:
                continue
            features = create_features_simple(duration, miles, receipts)
            if features is not None:
                records.append(features)
                y_targets.append(expected_output)
        if not records:
            print("No valid records after processing cases in load_training_data.")
            return None, None
        return pd.DataFrame(records), np.array(y_targets)
    except Exception as e:
        print(f"Error loading training data: {e}")
        return None, None


def save_model(model, score, model_name, params, feature_order):
    global joblib, m2c, np
    if joblib is None or m2c is None or np is None:
        print("Critical Error: joblib, m2cgen or NumPy not loaded before calling save_model.")
        sys.exit(1)
    ensure_model_dir()
    ensure_m2cgen_output_dir()
    joblib.dump(model, MODEL_PATH)
    header = '# Features order: ' + ', '.join(feature_order) + '\n'
    model_info = {
        'score': score, 'model_name': model_name, 'params': params,
        'timestamp': str(np.datetime64('now')), 'feature_order': feature_order
    }
    with open(MODEL_INFO_PATH, 'w') as f: json.dump(model_info, f, indent=2)
    print(f"Model saved to {MODEL_PATH}")
    print(f"Model info saved to {MODEL_INFO_PATH}")

    print(f"Exporting model to Python code using m2cgen... Features: {feature_order}")
    code = m2c.export_to_python(model)
    with open(M2CGEN_MODEL_PATH, 'w') as f: f.write(header + code)
    print(f'Model exported to {M2CGEN_MODEL_PATH}')


def train_optimized_model():
    global XGBRegressor, RandomForestRegressor, KFold, GridSearchCV, cross_val_score, train_test_split, mean_absolute_error, np
    if not all([XGBRegressor, RandomForestRegressor, KFold, GridSearchCV, cross_val_score, train_test_split, mean_absolute_error, np]):
         print("Critical Error: Essential ML modules not loaded before calling train_optimized_model.")
         sys.exit(1)

    X, y = load_training_data()
    if X is None or y is None or X.empty or y.size == 0:
        print("Training data is not available or empty. Exiting training.")
        return None, None, None
    feature_names = list(X.columns)
    print(f"Training on {len(X)} samples with {X.shape[1]} features: {feature_names}")

    models_config = {
        'xgb_fixed': XGBRegressor(max_depth=5, n_estimators=300, learning_rate=0.1, subsample=0.8, colsample_bytree=0.8, random_state=42, base_score=0, objective='reg:squarederror'),
        'xgb_tuned': XGBRegressor(random_state=42, base_score=0, objective='reg:squarederror'),
        'rf': RandomForestRegressor(random_state=42)
    }
    param_grids = {
        'rf': {'max_depth': [10], 'n_estimators': [50]},
        'xgb_fixed': {},
        'xgb_tuned': {
            'learning_rate': [0.01, 0.02, 0.04, 0.05, 0.1],
            'max_depth': [4, 5, 6, 7],
            'n_estimators': [300, 400, 500, 600, 700, 800],
            'subsample': [0.7, 0.8, 0.9, 1.0],
            'colsample_bytree': [0.7, 0.8, 0.9, 1.0],
            'random_state': [42],
            'base_score': [0],
            'objective': [
                'reg:squarederror',
            ]
        }
    }
    best_model_obj, best_score_val, best_model_name_val, best_params_val = None, float('inf'), None, None

    # Ensure X.shape[0] is appropriate for n_splits
    # KFold requires n_splits <= n_samples.
    # If only 1 sample, KFold cannot be used.
    num_samples = X.shape[0]
    n_cv_splits = min(10, num_samples) if num_samples > 1 else 1

    if num_samples < 2 : # Cannot do any CV with less than 2 samples.
        print("Dataset too small for any cross-validation (<2 samples). Using simplified training.")
        kfold = None # Explicitly set kfold to None
    elif n_cv_splits == 1 and num_samples == 1: # Still can't use KFold if only 1 sample.
         print("Dataset has only 1 sample. Using simplified training (no CV).")
         kfold = None
    else:
        kfold = KFold(n_splits=n_cv_splits, shuffle=True, random_state=42)


    if kfold is None:
        model_name_val = 'xgb_fixed'
        best_model_obj = models_config[model_name_val]
        best_model_obj.fit(X,y)
        predictions = best_model_obj.predict(X)
        best_score_val = mean_absolute_error(y, predictions)
        best_params_val = best_model_obj.get_params()
        best_model_name_val = model_name_val
        print(f"Simplified training for {model_name_val}. MAE on training data: {best_score_val:.2f}")
    else:
        for model_key, model_instance in models_config.items():
            print(f"\nTuning {model_key}...")
            current_param_grid = param_grids[model_key]
            if current_param_grid:
                # For XGBoost with early stopping, we need eval_set during GridSearchCV
                if isinstance(model_instance, XGBRegressor) and 'early_stopping_rounds' in current_param_grid:
                    # Split data for early stopping evaluation during GridSearchCV
                    X_train_cv, X_val_cv, y_train_cv, y_val_cv = train_test_split(X, y, test_size=0.2, random_state=42)

                    best_score_cv = float('inf')
                    best_params_for_model = None

                    # Manual grid search with early stopping
                    import itertools
                    param_combinations = list(itertools.product(*current_param_grid.values()))
                    param_names = list(current_param_grid.keys())

                    for param_combo in param_combinations:
                        params = dict(zip(param_names, param_combo))
                        esr = params.pop('early_stopping_rounds', None)

                        # Create model with these params
                        temp_model = model_instance.__class__(**params)

                        if esr is not None:
                            # Fit with early stopping
                            temp_model.fit(X_train_cv, y_train_cv,
                                         early_stopping_rounds=esr,
                                         eval_set=[(X_val_cv, y_val_cv)],
                                         verbose=False)
                        else:
                            temp_model.fit(X_train_cv, y_train_cv)

                        # Evaluate on validation set
                        pred = temp_model.predict(X_val_cv)
                        score = mean_absolute_error(y_val_cv, pred)

                        if score < best_score_cv:
                            best_score_cv = score
                            best_params_for_model = params.copy()
                            if esr is not None:
                                best_params_for_model['early_stopping_rounds'] = esr

                    # Create best model
                    final_params = best_params_for_model.copy()
                    esr_final = final_params.pop('early_stopping_rounds', None)
                    best_estimator_for_model = model_instance.__class__(**final_params)

                    if esr_final is not None:
                        best_estimator_for_model.fit(X_train_cv, y_train_cv,
                                                   early_stopping_rounds=esr_final,
                                                   eval_set=[(X_val_cv, y_val_cv)],
                                                   verbose=False)
                    else:
                        best_estimator_for_model.fit(X, y)

                    model_cv_score = best_score_cv
                else:
                    # Regular GridSearchCV for non-XGBoost or XGBoost without early stopping
                    grid_search = GridSearchCV(model_instance, current_param_grid, cv=kfold, scoring='neg_mean_absolute_error', n_jobs=-1, verbose=1)
                    grid_search.fit(X, y)
                    best_estimator_for_model = grid_search.best_estimator_
                    best_params_for_model = grid_search.best_params_
                    model_cv_score = -grid_search.best_score_
            else:
                cv_scores_array = cross_val_score(model_instance, X, y, cv=kfold, scoring='neg_mean_absolute_error', n_jobs=-1, verbose=1) # n_jobs=1
                model_cv_score = -np.mean(cv_scores_array)
                best_estimator_for_model = model_instance.fit(X,y)
                best_params_for_model = model_instance.get_params()
            print(f"{model_key} - CV MAE: {model_cv_score:.2f}")
            if not current_param_grid: print(f"{model_key} - Using predefined params.")
            else: print(f"{model_key} - Best params from GridSearch: {best_params_for_model}")
            if model_cv_score < best_score_val:
                best_score_val, best_model_obj, best_model_name_val, best_params_val = model_cv_score, best_estimator_for_model, model_key, best_params_for_model

    if best_model_obj is None: return None, None, None
    print(f"\nBest model selected: {best_model_name_val} with CV MAE: {best_score_val:.2f}")

    # Final fitting on all data - early stopping already handled during grid search
    print(f"\nFinal fit of best model {best_model_name_val} on all training data...")

    if isinstance(best_model_obj, XGBRegressor) and best_params_val and 'early_stopping_rounds' in best_params_val:
        # If the best model used early stopping, refit with same parameters on all data
        esr = best_params_val['early_stopping_rounds']
        if esr is not None and X.shape[0] >= 10:  # Need enough data for train/val split
            X_train_final, X_val_final, y_train_final, y_val_final = train_test_split(X, y, test_size=0.2, random_state=42)

            # Create fresh model with best params (excluding early_stopping_rounds)
            final_params = {k: v for k, v in best_params_val.items() if k != 'early_stopping_rounds'}
            final_model = best_model_obj.__class__(**final_params)

            final_model.fit(X_train_final, y_train_final,
                          early_stopping_rounds=esr,
                          eval_set=[(X_val_final, y_val_final)],
                          verbose=False)
            best_model_obj = final_model
            print(f"Final model refit with early stopping (rounds={esr})")
        else:
            # Fallback to regular fit if not enough data
            best_model_obj.fit(X, y)
            print("Final model fit without early stopping (insufficient data)")
    else:
        # Regular fit for non-XGBoost or XGBoost without early stopping
        if hasattr(best_model_obj, 'fit'):
            best_model_obj.fit(X, y)
        print("Final model fit complete")

    if hasattr(best_model_obj, 'feature_importances_'):
        importances = best_model_obj.feature_importances_
        top_features = sorted(zip(feature_names, importances), key=lambda x: x[1], reverse=True)
        print(f"\nTop {len(top_features)} feature importances for {best_model_name_val}:")
        for feature, importance in top_features: print(f"  {feature}: {importance:.4f}")

    final_params_to_save = best_model_obj.get_params()
    save_model(best_model_obj, best_score_val, best_model_name_val, final_params_to_save, feature_names)
    return best_model_obj, best_score_val, feature_names


def get_model_status():
    global joblib
    if joblib is None:
        print("Critical Error: joblib module not loaded.")
        return "Model libraries not loaded."
    if not os.path.exists(MODEL_INFO_PATH): return "No saved model found"
    try:
        with open(MODEL_INFO_PATH, 'r') as f: model_info = json.load(f)
        status = f"Saved Model Information:\n- Model Type: {model_info.get('model_name', 'N/A')}\n- CV MAE: {model_info.get('score', float('nan')):.2f}\n"
        status += f"- Feature Order: {model_info.get('feature_order', [])}\n- Trained At: {model_info.get('timestamp', 'N/A')}\n"
        status += f"- Model File: {MODEL_PATH}\n- M2CGEN File: {M2CGEN_MODEL_PATH}"
        return status
    except Exception as e: return f"Error reading model info: {e}"

def delete_saved_model():
    try:
        files_to_delete = [MODEL_PATH, MODEL_INFO_PATH, M2CGEN_MODEL_PATH]
        for file_path in files_to_delete:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
        if os.path.exists(M2CGEN_OUTPUT_DIR) and not os.listdir(M2CGEN_OUTPUT_DIR):
            os.rmdir(M2CGEN_OUTPUT_DIR)
            print(f"Deleted empty directory: {M2CGEN_OUTPUT_DIR}")
        if os.path.exists(MODEL_DIR) and not os.listdir(MODEL_DIR):
            os.rmdir(MODEL_DIR)
            print(f"Deleted empty directory: {MODEL_DIR}")
        return True
    except Exception as e:
        print(f"Error deleting saved model: {e}")
        return False

def load_saved_model():
    global joblib
    if joblib is None:
        print("Critical Error: joblib module not loaded.")
        return None, None, None, None
    if not (os.path.exists(MODEL_PATH) and os.path.exists(MODEL_INFO_PATH)): return None, None, None, None
    try:
        model = joblib.load(MODEL_PATH)
        with open(MODEL_INFO_PATH, 'r') as f: model_info = json.load(f)
        return model, model_info['score'], model_info['model_name'], model_info.get('feature_order')
    except Exception as e:
        print(f"Error loading saved model: {e}")
        return None, None, None, None

def main():
    global np, pd, m2c, XGBRegressor, RandomForestRegressor, KFold, GridSearchCV, cross_val_score, train_test_split, mean_squared_error, mean_absolute_error, joblib, re

    # Stdlib re is already imported at the top
    # print("DEBUG: Inside main(). Attempting to import libraries...") # Reduced verbosity
    try:
        import numpy as np
        import pandas as pd
        import m2cgen as m2c
        from xgboost import XGBRegressor
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.model_selection import KFold, GridSearchCV, cross_val_score, train_test_split
        from sklearn.metrics import mean_squared_error, mean_absolute_error
        import joblib
        # print("DEBUG: Successfully imported all ML libraries.")
    except ImportError as e:
        missing_package_match = re.search(r"No module named '(\w+)'", str(e))
        missing_package = missing_package_match.group(1) if missing_package_match else "a required library"
        print(f"Error: {missing_package} not found.")
        print("Attempting to install required ML libraries: xgboost, scikit-learn, m2cgen, pandas, numpy, joblib")
        try:
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "xgboost", "scikit-learn", "m2cgen", "pandas", "numpy", "joblib"])
            print("Installation attempt complete. Please re-run the script.")
            sys.exit(1)
        except Exception as install_e:
            print(f"Failed to auto-install packages: {install_e}")
            print("Please install them manually: pip install xgboost scikit-learn m2cgen pandas numpy joblib")
            sys.exit(1)

    parser = argparse.ArgumentParser(description='Manage the reimbursement ML model')
    parser.add_argument('action', choices=['status', 'train', 'delete', 'load'], help='Action to perform')
    args = parser.parse_args()

    # print(f"DEBUG: Action requested: {args.action}")
    if args.action == 'status':
        print("Model Status:"); print("=" * 50); print(get_model_status())
    elif args.action == 'train':
        print("Training new model..."); print("=" * 50)
        ensure_m2cgen_output_dir()
        model, score, _ = train_optimized_model()
        if model is not None:
            print(f"\n✅ Model trained successfully! CV MAE: {score:.2f}")
            print("Model saved and exported to Python code for fast inference.")
        else:
            print("\n❌ Failed to train model")
    elif args.action == 'delete':
        print("Deleting saved model..."); print("=" * 50)
        if delete_saved_model(): print("✅ Model deleted successfully")
        else:
            print("❌ Failed to delete model")
    elif args.action == 'load':
        print("Checking saved model..."); print("=" * 50)
        model, score, name, _ = load_saved_model()
        if model is not None: print(f"✅ Found saved model: {name} (CV MAE: {score:.2f})")
        else:
            print("❌ No saved model found. Run 'train' to create one.")

if __name__ == "__main__":
    # print("DEBUG: __name__ == '__main__' check passed.")
    main()
