import streamlit as st
import joblib
import pandas as pd
import numpy as np
import plotly.express as px

# Load model
model = joblib.load('models/best_model.pkl')

# UI values
locations = ['Nuwara Eliya', 'Kandy', 'Galle']
years = [2020, 2021, 2022]
varieties = ['UP1', 'CR2', 'TN1']

# UI
st.title("🌱 Tea Yield Prediction - Sri Lanka")

location = st.selectbox("📍 Location", locations)
year = st.selectbox("📅 Year", years)
variety = st.selectbox("🍃 Variety", varieties)

temp = st.slider("🌡️ Avg Temp (°C)", 15.0, 30.0, 22.0)
rain = st.slider("🌧️ Rainfall (mm)", 1000, 3000, 2000)
humidity = st.slider("💧 Humidity (%)", 50, 100, 80)
ph = st.slider("🧪 Soil pH", 4.0, 6.5, 5.0)
nitrogen = st.slider("🌿 Soil Nitrogen (%)", 0.05, 0.3, 0.15)

# Prepare input
input_dict = {
    'avg_temp (°C)': [temp],
    'rainfall (mm)': [rain],
    'humidity (%)': [humidity],
    'soil_ph': [ph],
    'soil_nitrogen (%)': [nitrogen],
    'location': [location],
    'variety': [variety]
}

input_df = pd.DataFrame(input_dict)
input_encoded = pd.get_dummies(input_df)

# Align with training
train_cols = model.feature_names_in_
for col in train_cols:
    if col not in input_encoded:
        input_encoded[col] = 0

input_encoded = input_encoded[train_cols]

# Predict
if st.button("Predict Yield"):
    result = model.predict(input_encoded)[0]

    # KPI Card
    col1, col2 = st.columns(2)
    col1.metric("🌱 Predicted Yield", f"{result:,.2f} kg/hectare")
    target = 2000
    delta = result - target
    col2.metric("🎯 Target Yield", f"{target} kg/hectare", delta=f"{delta:.2f}")

    # Bar Chart
    chart_df = pd.DataFrame({
        'Category': ['Predicted Yield'],
        'Yield': [result]
    })
    fig = px.bar(chart_df, x='Category', y='Yield', color='Category', text='Yield', range_y=[0, 3000])
    st.plotly_chart(fig, use_container_width=True)
