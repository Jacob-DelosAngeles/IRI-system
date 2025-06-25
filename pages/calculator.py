import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils.iri_calculator import IRICalculator

# Set page config
st.set_page_config(
    layout = "wide",
    initial_sidebar_state = "expanded"
)


# Custom CSS for template
st.markdown("""
<style>

    h1{
        text-align: center;
    }

    .info-box{
        background-color : #F8F9FA;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2E4057;
        margin: 1rem 0;
    }

    .section-header{
        font-size: 1.5rem;
        font-weight: bold;
        color: #2E4057
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #2E4057;
        padding-bottom: 0.5rem;
        text-align: left;
    }

    .metric-container{
        background-color: #E8F4FD;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem 0;
    }

    .stButton > button[kind="primary"]{
        background-color: #2E4057 !important;
        color: white;
        border: none;
        border-radius: 5 px;
        font-weight: bold;
        padding: 0.5rem 1rem;
    }

    st.Button > button[kind="primary"]{
        background-color: #1a2633;
        color:white;
    }

</style>

""", unsafe_allow_html = True)

st.markdown('<h1 class="main-header">📱 IRI Calculator</h1>',
unsafe_allow_html = True)

# Description
st.markdown("""
<div class="info-box">
    <h3>📊 Calculate International Roughness Index</h3>
    <p>Upload CSV sensor data exported from Physics Toolbos Sensor Suite
    to calculate the International Roughness Index (IRI) for your pavement section. This tool processes accelerometer data and applies 
    the RMS IRI calculation methodology.</p>
</div>
""", unsafe_allow_html = True)

# Instructions
st.markdown("<div class='section-header'>📋 Instructions </div>", unsafe_allow_html = True)

col1, col2 = st.columns([2,1])

with col1:
    st.markdown("""
    **Data Collection Setup:**
    1. Use Physics Toolbox Sensor Suite app on your smartphone
    2. Enable the **Linear Accelerometer**,  **Gyroscope**, and **GPS**
    3. Click "**+**" to record data
    4. Record Data while driving at consistent speed (50-80 km/hr)
    5. Export data as CSV format

    **File Requirements:**
    - CSV format with headers
    - Columns: time, ax, ay, az (acceleration data)
    - Maximum file size: 200 MB
    - Minimum recording duration: 30 seconds
    """, unsafe_allow_html = True)

with col2:
    st.markdown("""
    <div class="metric-container">
        <h4>📈 Expected Results</h4>
        <p><strong>IRI Values</strong> (m/km)</p>
        <p><strong>Quality Rating<strong></p>
        <p><strong>Visualization</strong></p>
        <p><strong>Statistics</strong></p>
    """, unsafe_allow_html = True)

# File upload section
st.markdown("<div class='section-header'>📂 Upload CSV File</div>",
unsafe_allow_html = True)

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=['csv'],
    help="Upload CSV sensor data exported from Physics Toolbox Sensor Suite",
    key = "csv_uploader"
)

if uploaded_file is not None:
    # Display file info
    st.success(f"✅ File Uploaded: {uploaded_file.name}")
    st.info(f"📊 File size: {uploaded_file.size / 1024 / 1024:.2f} MB")

    # Show processing status
    st.markdown('<div class="section-header">📊 Processing Status</div>', 
    unsafe_allow_html = True)

    st.info("""
    **File Analysis Complete:**
    
    Your CSV file has been successfully uploaded and is ready for processing.
    The IRI Calculation engine will analyze your acclerometer data using the 
    Root Mean Squared(RMS) model methodology to determine pavement roughness.

    **Processing Steps:**
    1. ✅ File validation and format verification
    2. ✅ Data cleaning and outlier removal
    3. ✅ Signal filtering and noise reduction
    4. ✅ Coordinate system alignment
    5. ✅ RMS model application
    6. ✅ IRI calculation and quality assessment
    """)

    # Calculate Button and algorithm
    if st.button("🧮 Caculate IRI", type="primary", use_container_width = True):
        with st.spinner("Processing accelerometer data and calculating IRI..."):
            import time
            time.sleep(2) # Simulate processing time

            # Include the Program for calculation
            iri_calc = IRICalculator()
            df = pd.read_csv(uploaded_file)
            df_processed, duration = iri_calc.preprocess_data(df)

            if df_processed is not None:
                
                # For IRI Calculation
                iri_values, segments, sampling_rate, speed = iri_calc.calculate_iri_rms_method(df_processed, segment_length = 150)

                mean_iri = np.mean(iri_values)

                # For Total Distance
                segment_centers = [s['distance_start'] + s['length']/2 for s in segments]
                total_distance = segment_centers[-1] + (segments[-1]['length']/2)


                # Formatted Results
                st.markdown('<div class="section-header">🏆 IRI Calculation Results</div>',
                unsafe_allow_html = True)

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("🛣️ IRI Value", f"{mean_iri:.2f}", help="International Roughness Index")
                with col2:
                    if mean_iri <= 3:
                        classification = 'Good'
                    elif mean_iri <= 5:
                        classification = 'Fair'
                    elif mean_iri <= 7:
                        classification = 'Poor'
                    else:
                        classification = 'Bad'
                    st.metric("⭐ Road Quality", f"{classification}", help="Pavement quality assessment")
                with col3:
                    st.metric("📊 Standard Deviation", f"{np.std(iri_values):.2f}", help="IRI spread")
                
                # Quality Assessment
                def get_sample_quality_rating(iri_value):
                    if iri_value <= 3:
                        return{
                            'rating': 'Good',
                            'description': 'Acceptable pavement condition',
                            'color': '#28a745',
                            'interpretation': """This pavement provides good ride quality
                            with acceptable smoothness. Vehicle operating costs are within
                            normal range and user comfort is satisfactory.""",
                            'recommendations': """Condition with routine maintenance activities.
                            Monitor condition annually and apply preventive treatments as needed to maintain
                            current service level."""
                        }
                    elif iri_value <=5:
                        return{
                            'rating' : 'Fair',
                            'description': 'Moderate pavement roughness',
                            'color': '#ffc107',
                            'interpretation': """This pavement shows moderate roughness that begins
                            to affect ride quality. Some increase in vehicle operating costs and minor
                            user discomfort may be experienced.""",
                            'recommendations': """Plan for rehabilitation treatments within 3-5 years. Consider
                            surface treatments or minor structural improvements to prevent further deterioration."""
                        }
                    
                    elif iri_value <= 7:
                        return{
                            'rating': 'Poor',
                            'description': 'Significant pavement deterioration',
                            'color': '#fd7e14',
                            'interpretation': """This pavement has significant roughness that
                            notably impacts ride quality and increases vehicle operating costs. User
                            comfort is compromised  and maintenance costs are elevated.""",
                            'recommendations': """Prioritize major rehabilitation or reconstruction within 2-3 years.
                            Implement interim maintenance to prevent further rapid deterioration and safety issues."""
                        }
                    
                    else:
                        return{
                            'rating': 'Bad',
                            'description': 'Severe pavement distress',
                            'color': '#dc3545',
                            'interpretation': """This pavement exhibits severe roughness causing substantial user discomfort, high vehicle operating costs, 
                            and potential safety concerns. Structural integrity may be compromised.""",
                            'recommendations': """Immediate major rehabilitation or full reconstruction required. Consider emergency repairs if safety is compromised. Evaluate load restrictions
                            until permanent repairs are completed."""
                        }

                
                quality = get_sample_quality_rating(mean_iri)

                st.markdown(f"""
                <div class='info-box' style="border-left-color: {quality['color']};">
                    <h4>🎯 Quality Assessment</h4>
                    <p><strong>Rating:</strong> {quality['rating']} ({quality['description']})</p>
                    <p><strong>Interpretation:</strong> {quality['interpretation']}</p>
                    <p><strong>Recommendations:</strong> {quality['recommendations']}</p>
                </div>
                """, unsafe_allow_html=True)


                # Statistical Summary
                st.markdown('<div class="section-header">📊 Statistical Summary</div>', unsafe_allow_html = True)

                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**Calculation Parameters:**")
                    st.write(f"- Data Duration: {duration:.2f} seconds ")
                    st.write(f"- Sampling Rate: {sampling_rate:.2f} Hz")
                    st.write(f"- Speed Estimate: {(speed*3.6):.2f} km/h")
                    st.write(f"- Distance Covered: {(total_distance/1000):.2f} km")
                
                with col2:
                    st.markdown("**Data Quality Metrics:**")
                    st.write(f"- Min IRI: {np.min(iri_values):.2f} m/km ")
                    st.write(f"- Max IRI: {np.max(iri_values):.2f}  m/km")
                    st.write(f"- Standard Deviation: {np.std(iri_values):.2f} m/km")
                    st.write(f"- Road IRI: {mean_iri:.2f} m/km")

        
                # Plotting Results
                st.markdown('<div class="section-header">📈 IRI Data Visualization </div>', unsafe_allow_html = True)

                fig, ax = plt.subplots()
                ax.plot(segment_centers, iri_values, 'ro-')
                ax.set_xlabel("Distance (m)")
                ax.set_ylabel("IRI (m/km)")
                ax.set_title("International Roughness Index per 150 m")
                ax.grid(True)
                st.pyplot(fig)
            else:
                st.error("❌ Data preprocessing failed")


else:
    # Upload placeholder
    st.markdown("""
    <div style="border: 2px dashed #ccc; border-radius: 10px; padding: 2rem;
    text-align:center; margin: 2rem 0;">
        <h3>📁 Drag and Drop File Here</h3>
        <p>or use the file browser</p>
        <p><em>Limit 200MB per file  •  CSV format only</em></p>
    </div>
    """, unsafe_allow_html = True)
