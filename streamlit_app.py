import streamlit as st
import pandas as pd
import numpy as np

st.title('🛣️IRI Calculator')

st.markdown(
    "<span style = 'font-size: 16px; color:gray;'>"
    "International Roughness Index (IRI) is a global standard for evaluating road smoothness. "
    "It measures how much a vehicle bounces at it moves, based on vertical acceleration data."
    "</span>",
    unsafe_allow_html=True
    )
st.write('Upload CSV sensor data exported from Physics Toolbox Sensor Suite')

# File upload 
uploaded_file = st.file_uploader("Choose a CSV file", type='csv')

# Tabulate data
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Raw Data Preview", df.head())

    st.success("File Uploaded and Processed")

    # Input Formula for Calculation of IRI

