import streamlit as st

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
        text-align: center
        margin: 0.5rem 0;
        text-align: center;
    }

</style>
""", unsafe_allow_html = True)

# Adding the Title
st.markdown('<h1 class="main-header">International Roughness Index</h1>', unsafe_allow_html=True)

# Introduction Section
st.markdown("""
<div class = "info-box">
    <h3>🛣️ Welcome to the IRI Calculator</h3>
    <p>The International Roughness Index (IRI) is a 
    globally recognized standard for evaluating 
    road surface quality and ride comfort. This application
    helps pavement engineers and transportation
    professionals calculate IRI values from 
    accelerometer sensor data.
    </p>
</div>
""", unsafe_allow_html = True)

# What is the IRI section
st.markdown("""<div class="section-header"> What is the 
International Roughness Index</div>""", unsafe_allow_html=True)

col1, col2 = st.columns([2,1])
with col1:
    st.markdown("""
    The International Roughness Index (IRI) is a standardized measure of road surface irregularities
    that affect vehicle road quality, fuel consumption,
    and maintenanance costs. It quantifies the cumulative vertical displacement
    of a vehicle's suspension system when traveling over a road surface

    **Key Characteristics:**
    - **Units**: Meters per kilometer (m/km) or millimeters per meter (mm/m)
    - **Scale**: Typically ranges from 0 (perfectly smooth) to 20+ (extremely rough)
    - **Standard**: Defined by the World Bank and widely adopted globally
    - **Applications**: Pavement management, construction quality control, research
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class = "metric-container">
        <h4>IRI Quality Scale</h4>
        <p><strong>0-1.5</strong> - Excellent</p>
        <p><strong>1.5-3.0</strong> - Good</p>
        <p><strong>3.0-4.5</strong> - Fair</p>
        <p><strong>4.5-6.0</strong> - Poor</p>
        <p><strong>6.0+</strong> - Very Poor
    </div>
    """, unsafe_allow_html = True)

# Technical Background
st.markdown('<div class="section-header">Technical Background</div>', unsafe_allow_html =True)

st.markdown("""
<div class = "info-box">
    <h4>🔬 Measurement Methodology</h4>
    <p> IRI is calculated using a mathematical model that simulates 
    a quarter-car vehicle traveling a 80 km/hr over the measured road profile.
    The model considers:</p>
    <ul>
        <li><strong>Suspension Dynamics</strong> - Spring and damper characterics</li>
        <li><strong>Tire Properties</strong> - Contact patch and compliance</li>
        <li><strong>Vehicle Mass</strong> - Sprung and unsprung massed</li>
        <li><strong>Speed Normalization</strong> - Standardized to 80 km/h reference</li>
    </ul>
</div>
""", unsafe_allow_html = True)