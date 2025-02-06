import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the trained model
model = joblib.load("mental_health_model.pkl")

# Streamlit UI Enhancements
st.set_page_config(page_title="Mental Health Predictor", page_icon="🧠", layout="centered")

# Header Section
st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>🧠 Mental Health Condition Predictor</h1>
    <h4 style='text-align: center; color: gray;'>A machine learning tool to assess mental health risks at work</h4>
    <hr>
    """, 
    unsafe_allow_html=True
)

# Sidebar for Input
st.sidebar.header("🔹 User Input Features")
st.sidebar.write("Fill in the details below:")

# *Dropdown values mapped to user-friendly text*
work_interfere_options = {
    "Never (0)": 0, "Rarely (1)": 1, "Sometimes (2)": 2, "Often (3)": 3
}
family_history_options = {"No (0)": 0, "Yes (1)": 1}
care_options_options = {"No (0)": 0, "Yes (1)": 1}
gender_options = {"Male (1)": 1, "Female (2)": 2, "Other (3)": 3}
country_options = {"USA (1)": 1, "Canada (2)": 2, "India (3)": 3, "UK (4)": 4, "Other (5)": 5}
no_employees_options = {
    "1-5 (1)": 1, "6-25 (2)": 2, "26-100 (3)": 3, "101-500 (4)": 4, "500+ (5)": 5
}
leave_options = {"No (0)": 0, "Yes (1)": 1}
benefits_options = {"No (0)": 0, "Yes (1)": 1}
mental_health_consequence_options = {"No (0)": 0, "Yes (1)": 1}

# *Collect user inputs with readable dropdowns*
work_interfere = st.sidebar.selectbox("🔹 Work Interference", list(work_interfere_options.keys()), help="How often does mental health interfere with work?")
Age = st.sidebar.number_input("🔹 Age", min_value=10, max_value=100, value=25, help="Enter your age.")
family_history = st.sidebar.selectbox("🔹 Family History", list(family_history_options.keys()), help="Does your family have a history of mental health issues?")
care_options = st.sidebar.selectbox("🔹 Care Options", list(care_options_options.keys()), help="Are mental health care options available at work?")
Gender = st.sidebar.selectbox("🔹 Gender", list(gender_options.keys()), help="Select your gender.")
Country = st.sidebar.selectbox("🔹 Country", list(country_options.keys()), help="Choose your country.")
no_employees = st.sidebar.selectbox("🔹 Company Size", list(no_employees_options.keys()), help="How many employees work at your company?")
leave = st.sidebar.selectbox("🔹 Leave for Mental Health", list(leave_options.keys()), help="Can you take leave for mental health reasons?")
benefits = st.sidebar.selectbox("🔹 Workplace Benefits", list(benefits_options.keys()), help="Does your workplace offer mental health benefits?")
mental_health_consequence = st.sidebar.selectbox("🔹 Fear of Negative Consequences", list(mental_health_consequence_options.keys()), help="Do you fear negative consequences if you discuss mental health?")

# *Convert user-friendly labels back to numerical values*
user_input_df = pd.DataFrame([[
    work_interfere_options[work_interfere],
    Age,
    family_history_options[family_history],
    care_options_options[care_options],
    gender_options[Gender],
    country_options[Country],
    no_employees_options[no_employees],
    leave_options[leave],
    benefits_options[benefits],
    mental_health_consequence_options[mental_health_consequence]
]], columns=["work_interfere", "Age", "family_history", "care_options",
             "Gender", "Country", "no_employees", "leave", "benefits", "mental_health_consequence"])

# Predict button
st.markdown("<hr>", unsafe_allow_html=True)
st.write("### 🔎 Click the button below to get your mental health prediction.")

if st.button("💡 Predict Mental Health Condition"):
    prediction = model.predict(user_input_df)
    probabilities = model.predict_proba(user_input_df)  # Get confidence scores

    # Define condition labels
    condition_labels = {0: "✅ No Major Concerns", 1: "⚠️ Needs Mental Health Support"}
    predicted_condition = condition_labels.get(prediction[0], "Unknown Condition")

    # Display Result
    st.markdown(f"<h2 style='text-align: center; color: #FF5733;'>{predicted_condition}</h2>", unsafe_allow_html=True)

    # Show probability scores
    st.write("### 🔢 Prediction Confidence:")
    st.write(f"- *No Major Concerns (0):* {probabilities[0][0]*100:.2f}%")
    st.write(f"- *Needs Mental Health Support (1):* {probabilities[0][1]*100:.2f}%")

    # Display message based on prediction
    if prediction[0] == 1:
        st.warning("⚠️ Consider speaking to a mental health professional.")
    else:
        st.success("✅ You seem to be doing well, but always prioritize mental well-being!")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: gray;'>Developed with ❤️</h5>", unsafe_allow_html=True)
