import os
import sys
# Ensure scikit-learn, joblib and numpy are installed
# This is a temporary measure for the execution environment.
# In a real project, these would be in requirements.txt or similar.
print("Ensuring scikit-learn, joblib, and numpy are installed...")
# Use sys.executable to ensure pip is run for the correct Python interpreter
install_command = f"{sys.executable} -m pip install scikit-learn joblib numpy"
print(f"Executing: {install_command}")
exit_code = os.system(install_command)
if exit_code == 0:
    print("Installation/check successful.")
else:
    print(f"Installation command failed with exit code {exit_code}. This might lead to import errors.")

# Now, import the libraries
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.metrics import mean_squared_error # Though GridSearchCV can use string names for scorers
import joblib
import json # For dummy data creation

# Assuming load_data.py and feature_engineering.py are in the same directory or PYTHONPATH
import load_data
import feature_engineering

def train_model(data_file_path: str, model_output_path: str):
    """
    Loads data, trains a DecisionTreeRegressor model using GridSearchCV, and saves the best model.

    Args:
        data_file_path: Path to the JSON data file.
        model_output_path: Path where the trained model will be saved.

    Returns:
        The best trained model.
    """
    print(f"Loading data from: {data_file_path}")
    initial_features, targets, raw_inputs = load_data.load_data(data_file_path)

    print("Engineering features...")
    # Ensure features are numpy arrays of floats for scikit-learn
    X_engineered = feature_engineering.engineer_features(raw_inputs, initial_features)
    X = np.array(X_engineered, dtype=np.float64)
    y = np.array(targets, dtype=np.float64)

    if X.shape[0] == 0:
        print("No data loaded. Aborting training.")
        return None
    if X.shape[0] != y.shape[0]:
        print(f"Mismatch in number of samples between features ({X.shape[0]}) and targets ({y.shape[0]}). Aborting.")
        return None

    print(f"Data loaded: {X.shape[0]} samples, {X.shape[1]} features per sample.")

    param_grid = {
        'max_depth': [None, 5, 10, 15, 20], # Reduced for faster example run
        'min_samples_split': [2, 5, 10],    # Reduced for faster example run
        'min_samples_leaf': [1, 2, 5],      # Reduced for faster example run
        'criterion': ['squared_error', 'absolute_error']
    }

    # Using a smaller n_splits for faster example run if dataset is small
    n_cv_splits = min(5, X.shape[0] if X.shape[0] > 1 else 2) # Ensure at least 2 splits if possible
    if X.shape[0] < 2 : # KFold requires at least 2 samples for any splits
        print("Not enough samples to perform K-Fold cross-validation. Consider more data.")
        # Fallback: train on all data without CV, or handle as error
        # For this example, we'll try to train without CV if too few samples.
        # However, GridSearchCV requires cv.
        if X.shape[0] < n_cv_splits and X.shape[0] >=1 : # If samples are less than desired splits but >=1
             n_cv_splits = X.shape[0] # Use LeaveOneOut CV effectively if n_samples < n_splits
             if n_cv_splits == 1: # GridSearchCV does not support 1 split.
                 print("Only 1 sample available. Cannot perform GridSearchCV. Training a default model.")
                 model = DecisionTreeRegressor(random_state=42)
                 model.fit(X,y)
                 joblib.dump(model, model_output_path)
                 print(f"Trained model (default due to 1 sample) saved to {model_output_path}")
                 return model


    print(f"Setting up K-Fold Cross Validation with n_splits={n_cv_splits}")
    cv = KFold(n_splits=n_cv_splits, shuffle=True, random_state=42)

    print("Initializing GridSearchCV...")
    # n_jobs=-1 uses all processors. verbose=1 gives some output.
    grid_search = GridSearchCV(
        estimator=DecisionTreeRegressor(random_state=42),
        param_grid=param_grid,
        cv=cv,
        scoring='neg_mean_squared_error', # Negative MSE because GridSearchCV maximizes score
        n_jobs=-1,
        verbose=1
    )

    print("Fitting GridSearchCV to the data... This may take a while.")
    try:
        grid_search.fit(X, y)
    except ValueError as e:
        print(f"Error during GridSearchCV fit: {e}")
        print("This can happen if the number of samples is too small for the chosen cv splits.")
        # Example: if n_samples=3 and n_splits=5, it will fail.
        # The code above tries to adjust n_cv_splits, but edge cases might remain.
        return None


    best_model = grid_search.best_estimator_
    print(f"\nBest parameters found: {grid_search.best_params_}")
    print(f"Best cross-validation score (Negative MSE): {grid_search.best_score_}")

    print(f"Saving trained model to {model_output_path}...")
    joblib.dump(best_model, model_output_path)
    print(f"Trained model saved to {model_output_path}")

    return best_model

if __name__ == "__main__":
    # Define file paths
    data_file = "public_cases.json"
    model_file = "tree_regressor_model.joblib"

    # The script now expects 'public_cases.json' (or the specified data_file) to exist.
    # load_data.py (called by train_model) will handle opening it.
    print(f"Starting model training with data from: {data_file}, output to: {model_file}")

    # Train the model
    trained_model = train_model(data_file, model_file)

    if trained_model:
        print("Model training process completed.")
    else:
        print("Model training failed or was aborted.")
