import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open("Concrete.pkl", "rb"))

# UI Design
st.set_page_config(page_title="Concrete Strength Predictor", layout="centered")

# Top Left: Company Name

# Title and Domain Name
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Concrete Strength Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: #555;'>Structural Engineering and Material Science</h5>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Enter the details below to predict the strength</h4>", unsafe_allow_html=True)

# Input fields
cement = st.number_input("Cement (kg/m³)", min_value=0.0, format="%.2f")
slag = st.number_input("Slag (kg/m³)", min_value=0.0, format="%.2f")
ash = st.number_input("Fly Ash (kg/m³)", min_value=0.0, format="%.2f")
water = st.number_input("Water (kg/m³)", min_value=0.0, format="%.2f")
superplastic = st.number_input("Superplasticizer (kg/m³)", min_value=0.0, format="%.2f")
coarseagg = st.number_input("Coarse Aggregate (kg/m³)", min_value=0.0, format="%.2f")
fineagg = st.number_input("Fine Aggregate (kg/m³)", min_value=0.0, format="%.2f")
age = st.number_input("Age (Days)", min_value=1, format="%d")

# Predict button
if st.button("Predict Strength"):
    input_data = np.array([[cement, slag, ash, water, superplastic, coarseagg, fineagg, age]])
    prediction = model.predict(input_data)[0]
    
    st.success(f"Predicted Concrete Strength: {prediction:.2f} MPa")
    
    st.markdown("<h3 style='text-align: center; color: #FF5733;'>Amazing Prediction!</h3>", unsafe_allow_html=True)
