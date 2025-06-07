import os
import sys

# Ensure m2cgen is installed
# This is a temporary measure for the execution environment.
print("Ensuring m2cgen is installed...")
install_command = f"{sys.executable} -m pip install m2cgen joblib" # joblib also needed to load model
print(f"Executing: {install_command}")
exit_code = os.system(install_command)
if exit_code == 0:
    print("Installation/check successful for m2cgen and joblib.")
else:
    print(f"Installation command failed with exit code {exit_code}. This might lead to import errors.")

# Now, import the libraries
import joblib
import m2cgen # This import should now work

def convert_model_to_code(model_path: str, output_python_file_path: str):
    """
    Loads a trained model and converts it to plain Python code using m2cgen.

    Args:
        model_path: Path to the saved (joblib) trained model.
        output_python_file_path: Path where the generated Python code will be saved.
    """
    print(f"Loading model from: {model_path}")
    try:
        model = joblib.load(model_path)
    except FileNotFoundError:
        print(f"Error: Model file not found at {model_path}. Please ensure train_model.py has run successfully.")
        return
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    print(f"Successfully loaded model: {type(model)}")

    print("Converting model to Python code using m2cgen...")
    try:
        code = m2cgen.export_to_python(model)
    except Exception as e:
        print(f"Error during m2cgen conversion: {e}")
        return

    print(f"Saving generated Python code to: {output_python_file_path}")
    try:
        with open(output_python_file_path, "w") as f:
            f.write(code)
        print(f"Model successfully converted to Python code and saved to {output_python_file_path}")
    except IOError as e:
        print(f"Error saving generated code to file: {e}")

if __name__ == "__main__":
    model_file = "tree_regressor_model.joblib"  # Should be created by train_model.py
    output_code_file = "reimbursement_model.py"

    # Convert the model
    convert_model_to_code(model_file, output_code_file)

    # Verification step: Try to import and use the generated function
    # The generated file might be in the current directory.
    # Ensure Python can find it (it should if run from the same directory).
    print("\nAttempting to verify the generated model code...")
    try:
        # To import from a dynamically created .py file, we might need to be careful with paths
        # If convert_model.py and reimbursement_model.py are in /app/, it should work.
        from reimbursement_model import score as score_func
        print("Successfully imported 'score' function from generated model.")

        # Test with dummy data. The model was trained on 5 features:
        # trip_duration_days, miles_traveled, total_receipts_amount, miles_per_day, receipt_cents
        # Example: [days, miles, receipts, miles/day, cents]
        # Let's use values that might be sensible: e.g., 5 days, 200 miles, $150.75 total
        # miles_per_day = 200/5 = 40
        # receipt_cents = 75
        dummy_input_features = [5.0, 200.0, 150.75, 40.0, 75.0]

        # Check if the function is callable and produces a numerical output
        prediction = score_func(dummy_input_features)
        print(f"Test prediction with dummy data {dummy_input_features}: {prediction} (type: {type(prediction)})")
        if not isinstance(prediction, (int, float)):
             print("Warning: Prediction from score function is not a number (int/float).")

    except ImportError:
        print(f"Failed to import 'score' function from {output_code_file}. Check m2cgen output or file path.")
    except AttributeError:
        print(f"Successfully imported '{output_code_file}', but 'score' function not found. Check m2cgen output.")
    except Exception as e:
        print(f"An error occurred during verification: {e}")
