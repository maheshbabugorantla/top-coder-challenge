#!/bin/bash

# Ensure Python 3 is available
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found, please install it."
    exit 1
fi

# Step 1: Train the model
echo "Training the model..."
python3 train_model.py
if [ ! -f tree_regressor_model.joblib ]; then
    echo "Model training failed. tree_regressor_model.joblib not found."
    exit 1
fi
echo "Model training complete."

# Step 2: Convert the model to Python code
echo "Converting the model to Python code..."
python3 convert_model.py
if [ ! -f reimbursement_model.py ]; then
    echo "Model conversion failed. reimbursement_model.py not found."
    exit 1
fi
echo "Model conversion complete."

# Step 3: Generate predictions using private_cases.json
echo "Generating predictions for private_cases.json..."
if [ ! -f private_cases.json ]; then
    echo "Error: private_cases.json not found. Please ensure it is in the root directory."
    # Create a dummy private_cases.json if it's missing, so the script can run till the end for testing purposes.
    echo '[{"input": {"trip_duration_days": 1, "miles_traveled": 100, "total_receipts_amount": 50.00}}]' > private_cases.json
    echo "Created a dummy private_cases.json for testing."
    # exit 1 # Optionally exit if private_cases.json is critical and shouldn't be dummied
fi

python3 main.py private_cases.json > results.json
if [ $? -ne 0 ]; then
    echo "Prediction generation failed."
    exit 1
fi

echo "Predictions generated and saved to results.json."
echo "run.sh execution complete."
