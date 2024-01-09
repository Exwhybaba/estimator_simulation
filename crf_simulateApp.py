#from CRF_simulation import Simu
import streamlit as st
import pandas as pd
import io

# Page Config
st.set_page_config(
    page_title="Estimator CRF-Simulated Data",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
)

# Title
st.title("Estimator CRF-Simulator")

# File Upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Main Content
if uploaded_file is not None:
    st.subheader("Input the number of samples to be simulated:")
    sample_no = st.number_input("Number of Samples", min_value=1, step=1, value=100)

    original_data = pd.read_csv(uploaded_file)

    # Display Original Data
    st.subheader("Original Data:")
    st.dataframe(original_data.head())

    # Simulate Data Button
    if st.button("Generate Simulated Data", key="generate_button"):
        simulated_data = Simu(original_data, sample_no)

        # Display Simulated Data
        st.subheader("Simulated Data:")
        st.dataframe(simulated_data.head())

        # Save simulated data to a CSV file
        filename = f"simulated_{sample_no}_{uploaded_file.name}"
        simulated_data.to_csv(filename, index=False, encoding='utf-8-sig')

        # Download Button
        st.subheader("Download Simulated Data:")
        csv_data = simulated_data.to_csv(index=False)
        st.download_button(
            label="Download Simulated Data",
            data=io.StringIO(csv_data).read(),
            file_name=filename,
            key='download_button',
            help="Click to download the simulated data"
        )
