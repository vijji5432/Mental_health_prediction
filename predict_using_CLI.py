import joblib
import pandas as pd
import numpy as np

# Load trained model
model = joblib.load("mental_health_model.pkl")

# Define feature list
# final_features = [
#     "work_interfere", "Age", "family_history", "care_options",
#     "Gender", "no_employees", "leave", "benefits", "mental_health_consequence"
# ]

# Take user input
user_input = []
print("Enter the following details:")

for feature in final_features:
    value = input(f"{feature}: ")
    user_input.append(float(value))

# Convert input to Pandas DataFrame
input_df = pd.DataFrame([user_input], columns=final_features)

# Predict
prediction = model.predict(input_df)
probabilities = model.predict_proba(input_df)  # Get prediction confidence

# Display results
print("\nPredicted Mental Health Condition:", prediction[0])
print("Confidence Scores (0 = No Concern, 1 = Needs Support):", probabilities)
