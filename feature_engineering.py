import math
# We will need load_data from load_data.py, and json to create a dummy file for testing
import json
# Assuming load_data.py is in the same directory or accessible in PYTHONPATH
# For now, to make the script runnable standalone for development,
# we might need to adjust sys.path or ensure load_data.py is found.
# However, the problem implies direct import is fine.
import load_data

def engineer_features(raw_inputs: list[dict], existing_features: list[list[float]]) -> list[list[float]]:
    """
    Engineers new features from raw input data and combines them with existing features.

    Args:
        raw_inputs: A list of dictionaries, where each dictionary is a raw input case.
        existing_features: A list of lists, where each inner list contains the initial features for a case.

    Returns:
        A list of lists, where each inner list is the new feature vector including engineered features.
    """
    engineered_features_list = []

    for i, raw_input_case in enumerate(raw_inputs):
        current_existing_features = existing_features[i]

        trip_duration_days = raw_input_case['trip_duration_days']
        miles_traveled = raw_input_case['miles_traveled']
        total_receipts_amount = raw_input_case['total_receipts_amount']

        # Calculate miles_per_day
        if trip_duration_days > 0:
            miles_per_day = miles_traveled / trip_duration_days
        else:
            miles_per_day = 0

        # Calculate receipt_cents
        # receipt_cents = round((total_receipts_amount - math.floor(total_receipts_amount)) * 100)
        # A more robust way to get cents without floating point issues for the fractional part:
        receipt_cents = int(round((total_receipts_amount * 100)) % 100)


        new_feature_vector = list(current_existing_features)  # Start with a copy of existing features
        new_feature_vector.extend([miles_per_day, float(receipt_cents)]) # Ensure receipt_cents is float if others are
        engineered_features_list.append(new_feature_vector)

    return engineered_features_list

if __name__ == "__main__":
    # The script now expects 'public_cases.json' to exist.
    # load_data.py will handle the file opening.
    dummy_file_path = "public_cases.json" # Or any other file path as needed

    # Load data using the function from load_data.py
    initial_features, targets, raw_inputs_data = load_data.load_data(dummy_file_path)

    # Engineer features
    final_features = engineer_features(raw_inputs_data, initial_features)

    print(f"Number of samples: {len(final_features)}")

    print("\nFirst 3 raw_input samples:")
    for i in range(min(3, len(raw_inputs_data))):
        print(raw_inputs_data[i])

    print("\nFirst 3 original feature samples:")
    for i in range(min(3, len(initial_features))):
        print(initial_features[i])

    print("\nFirst 3 final feature samples (after engineering):")
    for i in range(min(3, len(final_features))):
        print(final_features[i])

    if final_features:
        print(f"\nNumber of features before engineering (sample 0): {len(initial_features[0])}")
        print(f"Number of features after engineering (sample 0): {len(final_features[0])}")
    else:
        print("\nNo data to show feature counts.")
