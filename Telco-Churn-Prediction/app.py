import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('model.pkl', 'rb') as f:
    model_data = pickle.load(f)
    
model = model_data['model']
model_features = model_data['features']

st.title("📞 Telco Customer Churn Predictor")
st.markdown("Enter customer details below to predict the likelihood of churn and help business teams proactively retain users.")

# Create sidebar to collect user input
st.sidebar.header("Input Customer Data")

def user_input_features():
    tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)
    MonthlyCharges = st.sidebar.slider("Monthly Charges ($)", 18.0, 120.0, 50.0)
    TotalCharges = tenure * MonthlyCharges
    
    Contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    InternetService = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    TechSupport = st.sidebar.selectbox("Tech Support", ["Yes", "No", "No internet service"])

    # Convert user input into a DataFrame
    data = {
        'tenure': tenure,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges,
        'Contract_One year': 1 if Contract == "One year" else 0,
        'Contract_Two year': 1 if Contract == "Two year" else 0,
        'InternetService_Fiber optic': 1 if InternetService == "Fiber optic" else 0,
        'InternetService_No': 1 if InternetService == "No" else 0,
        'TechSupport_No internet service': 1 if TechSupport == "No internet service" else 0,
        'TechSupport_Yes': 1 if TechSupport == "Yes" else 0,
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# Display user input data
st.write("### Current Customer Features")
st.write(input_df)

# Align features with the model requirement (fill missing features with 0)
for col in model_features:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[model_features] # Ensure feature order matches the model

# Prediction button
if st.button("Predict Churn"):
    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)[0][1] * 100
    
    st.write("### Prediction Result")
    if prediction[0] == 1:
        st.error(f"⚠️ Warning: This customer has a high risk of churning! (Probability: {probability:.1f}%)")
    else:
        st.success(f"✅ Safe: This customer is currently stable. (Churn Probability: {probability:.1f}%)")