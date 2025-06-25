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
        color: #2E4057;
        margin-top: 32px;
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
    
    .highlight-text{
        background-color: #FFF3CD;
        padding: 0.5rem;
        border-radius: 5px;
        border-left: 3px solid #FFC107;
    }

    [data-testid="stSidebar"] {
        background-image: url("https://github.com/Jacob-DelosAngeles/IRI-system/blob/master/images/sidebar_background.jpg?raw=true");
        background-position: center;
        background-repeat: no-repeat;
    }

    [data-testid="stSidebar"] .css-1wvake5,
    [data-testid="stSidebar"] .css-16idsys,
    [data-testid="stSidebar"] .css-10trblm,
    [data-testid="stSidebar"] .css-1v0mbdj,
    [data-testid="stSidebar"] .css-1v3fvcr,
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span {
        color: white !important;
        font-weight: bold;
        font-size: 1.1rem;
    }

    [data-testid="stSidebar"] svg {
    fill: white !important;
    }

    [data-testid="stNavSectionHeader"] {
        color: white;
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
        <p><strong>≤ 3.0</strong> - Good</p>
        <p><strong>3.1 - 5.0</strong> - Fair</p>
        <p><strong>5.1 - 7.0</strong> - Poor</p>
        <p><strong>> 7.0</strong> - Bad</p>
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


# Data Collection Methods
st.markdown("<div class='section-header'>Data Collection Methods</div>", unsafe_allow_html = True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **📱 Smartphone Sensors**
    - Accelerometer data collection
    - Physics Toolbox Sensor Suite
    - Cost-effective solution
    - Suitable for preliminary assessments
    """)

with col2:
    st.markdown("""
    **🚗 Vehicle-Mounted Systems**
    - Professional profilometers
    - Laser-based measurements
    - High-precision data
    - Continuous monitoring
    """)

with col3:
    st.markdown("""
    **🛰️ Remote Sensing**
    - Satellite imagery analysis
    - LiDAR technology
    - Large-scale assessments
    - Network-level monitoring
    """)

# Applications section
st.markdown('<div class="section-header">Applications in Pavement Engineering</div>', unsafe_allow_html = True)

applications = [
    {
        "title": "🏗️ Construction Quality Control",
        "description": """Verify that newly constructed pavement meet smoothness 
        specifications and contract requirements."""
    },
    {
        "title": "📊 Pavement Management Systems",
        "description": """Monitor pavement conditions over time
        and prioritize maintenance and rehabilitation projects"""
    },
    {
        "title": "💰 Economic Analysis",
        "description": """Quantify user costs related to vehicle
        operating expenses and ride quality impacts."""
    },
    {
        "title": "🔬 Research and Development",
        "description": """Evaluate new materials, construction techniques,
        and maintenance strategies. """
    },
    {
        "title": "🚛 Fleet Management",
        "description": """Asses route conditions for logistics optimization
        and vehicle maintenance planning."""
    },
    {
        "title": "🌍 Infrastracture Assessment",
        "description": """Support decision-making for transportation
        infrastructure investments and policies"""
    } 
]

for i in range(0,len(applications), 2):
    col1, col2 = st.columns(2)

    with col1:
        app = applications[i]
        st.markdown(f"""
        <div class="info-box">
            <h4>{app['title']}</h4>
            <p>{app['description']}</p>
        </div>
        """, unsafe_allow_html = True)
    
    if i + 1 < len(applications):
        with col2:
            app = applications[i+1]
            st.markdown(f"""
            <div class="info-box">
                <h4>{app['title']}</h4>
                <p>{app['description']}</p>
            </div>
            """, unsafe_allow_html = True)

# Getting Started Section
st.markdown("""<div class='section-header'>Getting Started
with IRI Calculation</div>""", unsafe_allow_html = True)

st.markdown("""
<div class="highlight-text">
    <h4>📋 Data Requirements</h4>
    <p>To calculate IRI using this application, you'll need:</p>
    <ul>
        <li><strong>CSV file</strong> with accelerometer  data
        from Physics Toolbox Sensor Suite</li>
        <li><strong>Time-series data</strong> including vertical
        acceleration measurements</li>
        <li><strong>Sampling rate</strong> of at least 100 Hz for
        accurate results</li>
        <li><strong>Vehicle Speed</strong> information (recommended 50-80 km/hr)</li>
    </ul>
    <p><em> Ready to calculate IRI? Navigate to the IRI Calculate page using
    the sidebar menu.</em></p>
</div>
""", unsafe_allow_html = True)


# Footer
st.markdown('---')
st.markdown("""
<div style = "text-align:center; color: #666; margin-top: 2rem;">
    <p><strong>IRI Calculator</strong> - Professional Pavement Engineering Tool</p>
    <p>Developed for transportation professionals and pavement engineers</p>
</div>
""", unsafe_allow_html = True)