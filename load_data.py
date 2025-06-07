import json

def load_data(file_path: str) -> tuple[list[list[float]], list[float], list[dict]]:
    """
    Loads data from a JSON file, extracts features, targets, and raw inputs.

    Args:
        file_path: The path to the JSON data file.

    Returns:
        A tuple containing three lists: features, targets, and raw_inputs.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)

    features = []
    targets = []
    raw_inputs = []

    for i, case in enumerate(data):
        try:
            # Ensure 'input' key exists
            if 'input' not in case:
                print(f"Error: 'input' key missing in case number {i} in file {file_path}")
                # Optionally, skip this case or raise a more specific error
                # For now, let's try to continue, which might lead to issues if not handled by caller
                continue

            current_input = case['input']

            # Extract features
            feature_values = [
                current_input['trip_duration_days'],
                current_input['miles_traveled'],
                current_input['total_receipts_amount']
            ]
            features.append(feature_values)

            # Extract target, if available
            targets.append(case.get('expected_output'))

            # Store raw input
            raw_inputs.append(current_input)
        except KeyError as e:
            print(f"KeyError in case number {i} in file {file_path}: Missing key {e} in {case}")
            # Decide how to handle: skip case, fill with defaults, or re-raise
            # For now, just printing and potentially continuing with partial data
            continue
        except TypeError as e:
            print(f"TypeError in case number {i} in file {file_path}: {e}. Case data: {case}")
            # This might happen if 'input' is not a dictionary
            continue

    return features, targets, raw_inputs

if __name__ == "__main__":
    # The script will now expect 'public_cases.json' to exist in the same directory.
    # If it's intended to be used with a different file,
    # the file_path argument in load_data call should be changed.
    features, targets, raw_inputs = load_data("public_cases.json")

    print(f"Number of samples loaded: {len(features)}")
    print("\nFirst 3 feature samples:")
    for i in range(min(3, len(features))):
        print(features[i])

    print("\nFirst 3 target samples:")
    for i in range(min(3, len(targets))):
        print(targets[i])

    print("\nFirst 3 raw_input samples:")
    for i in range(min(3, len(raw_inputs))):
        print(raw_inputs[i])
