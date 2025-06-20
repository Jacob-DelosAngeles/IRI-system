import streamlit as st

# --- PAGE SETUP -----

home_page = st.Page(
    page = "pages/overview.py",
    title = "Homepage",
    icon = "📄",
    default = True

)

iri_calculator = st.Page(
    page = "pages/calculator.py",
    title = "IRI Calculator",
    icon = "🛣️"
)

# ------ Navigation with section --------------

pg = st.navigation(
    {
        "Home" : [home_page],
        "Projects" : [iri_calculator]
    }
)

# -------- Run Navigation -------
pg.run()