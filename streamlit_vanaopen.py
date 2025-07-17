import streamlit as st

pages = {
    "Rohefaktor lehed": [
        st.Page("stream2.py", title="Kalkulaator"),
        st.Page("loe_lisaks.py", title="Loe lisaks"),
    ],
}

st.logo(
    'tallinn.png',
)

st.set_page_config(
    page_title="Rohefaktori arvutamine",
    page_icon="🍃",
    #layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "See on Tallinna rohefaktori arvutamise kalkulaator"
    }
)

pg = st.navigation(pages)
pg.run()