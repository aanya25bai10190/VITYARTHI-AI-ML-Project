import streamlit as st
import joblib

# Load model
model = joblib.load("model/model.pkl")

st.title("Cardiovascular Disease Predictor")

# ---------------- INPUTS ---------------- #

# Age
age_years = st.number_input("Age (years)", min_value=1, max_value=120, value=25)
age = age_years * 365

# Gender
gender_option = st.selectbox("Gender", ["Female", "Male"])

if gender_option == "Female":
    gender = 1
else:
    gender = 2

# Height & Weight
height = st.number_input("Height (cm)", min_value=100, max_value=220, value=170)
weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)

# Blood Pressure
ap_hi = st.number_input("Systolic BP (High)", min_value=80, max_value=200, value=120)
ap_lo = st.number_input("Diastolic BP (Low)", min_value=60, max_value=140, value=80)

# Cholesterol
cholesterol = st.selectbox("Cholesterol", [1, 2, 3])  # 1 normal, 2 above, 3 high

# Glucose
gluc = st.selectbox("Glucose Level", [1, 2, 3])

# Lifestyle
# Smoking
smoke_option = st.selectbox("Do you smoke?", ["No", "Yes"])
smoke = 1 if smoke_option == "Yes" else 0

# Alcohol
alco_option = st.selectbox("Do you drink alcohol?", ["No", "Yes"])
alco = 1 if alco_option == "Yes" else 0

# Physical Activity
active_option = st.selectbox("Are you physically active?", ["Yes", "No"])
active = 1 if active_option == "Yes" else 0

# ---------------- PREDICTION ---------------- #

if st.button("Predict"):
    input_data = [[
        age, gender, height, weight,
        ap_hi, ap_lo,
        cholesterol, gluc,
        smoke, alco, active
    ]]

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("High Risk of Cardiovascular Disease")
    else:
        st.success("Low Risk of Cardiovascular Disease")