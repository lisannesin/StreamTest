import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import base64
import rohefaktor_lisa
import taotlusvaartus
from Classes.taotlusClass import TaotlusClass 
from Classes.pohiClass import RohearvutusPohi
import boonus

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg_image(image_file):
    bin_str = get_base64(image_file)
    bg_image = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(bg_image, unsafe_allow_html=True)

# Call the function with your image file
#set_bg_image('beauty.jpg')


st.title("Detailplaneeringu rohefaktori taotlusväärtuse määramine")
st.markdown("*Tallinna linna rohefaktori tööriist toetab  planeeritaval alal kõrgekvaliteedilise rohetaristu kavandamist. Kavandatava lahenduse ökoloogilise kvaliteedi hindamiseks on koostatud arvutustabel, mis aitab kaasa nõuetekohase arvutuse läbiviimisele. Alljärgnevalt on kirjeldatud, kuidas rohefaktori analüüs läbi viiakse. Esimese asjana on vajalik seadistada, kas arvutus tehakse detailplaneeringu või ehitusprojekti tasandil.*")

# Tööpäevade arv


st.logo(
    'tallinn.png',
)

##########################################################################################
#st.subheader("**Detailplaneeringu rohefaktori taotlusväärtuse määramine.**")
st.divider()
st.subheader("**1. Samm: Taotlusväärtuse määramine**")
st.divider()


col1, col2 = st.columns(2)
number = 0
option_arv = 0

with col1:
    number = st.number_input("**Kogu detailplaneeringuala pindala (m2)**",
    value = 0.0,
    placeholder = "Valige juhtotstarvete arv...",
    format="%0.1f",)

with col2:
    option_arv = st.selectbox(
    "**Planeeringualal kavandatud erinevate juhtotstarvete arv.**",
    (1, 2, 3),
    index=0,  # Sets default to first option (1)
    placeholder="Valige juhtotstarvete arv..."
    )
    

# Initialize Streamlit columns
col_juht1, col_juht2, col_juht3 = st.columns(3)

arvutustabel1 = RohearvutusPohi(3, 3)

# Juhtotstarve 1
with col_juht1:

    

    class1 = TaotlusClass(number=1, pindala=number)


    taotlusvaartus.callVaartus(class1)

    #st.write(klass) 


# Conditional logic for Juhtotstarve 2
if option_arv in [2, 3]:
    with col_juht2:

        arvutustabel2 = RohearvutusPohi(3, 3)

        class2 = TaotlusClass(number=2, pindala=number)

        taotlusvaartus.callVaartus(class2)

if option_arv in [3]:

    with col_juht3:

        arvutustabel3 = RohearvutusPohi(3, 3)

        class3 = TaotlusClass(number=3, pindala=number)

        taotlusvaartus.callVaartus(class3)

#####################################################################################################
st.divider()
st.subheader("**2. Samm: Rohefaktori arvutus**")
st.divider()




if "selected_sv" not in st.session_state:
    st.session_state.selected_sv = None  # Default state, no selection

# 📌 Check which arvutustabels exist
available_options = {
    "SV1": ":material/add: Juhtotstarve 1",
}

if "arvutustabel2" in globals():
    available_options["SV2"] = ":material/zoom_out: Juhtotstarve 2"

if "arvutustabel3" in globals():  # Check if the variable is defined
    available_options["SV3"] = ":material/zoom_out: Juhtotstarve 3"

# 📌 Segmented Control for selection (Only show available options)
selection = st.segmented_control(
    "Juhtotstarve valik:",
    options=list(available_options.keys()),  # Only show available options
    format_func=lambda option: available_options[option],  # Display icons with labels
    selection_mode="single",
)

# 📌 Update session state when segmented control is used
if selection:
    st.session_state.selected_sv = selection

# 📌 Run `rohefaktor_lisa.addJuht()` based on selection
if st.session_state.selected_sv:
    # 📌 Checkbox to toggle bonus factor calculations
    agree = st.checkbox("Boonusfaktorite arvutus")

    # 📌 Create two-column layout
    rohe1, rohe2 = st.columns(2)

    with rohe1:
        if st.session_state.selected_sv == "SV1":
            rohefaktor_lisa.addJuht(arvutustabel1, "SV1")
        elif st.session_state.selected_sv == "SV2":
            try:
                rohefaktor_lisa.addJuht(arvutustabel2, "SV2")
            except NameError:
                #st.warning("arvutustabel2 is not defined, using arvutustabel1 instead.")
                rohefaktor_lisa.addJuht(arvutustabel1, "SV1")  # Fallback to arvutustabel1
            #rohefaktor_lisa.addJuht(arvutustabel2, "SV2")
        elif st.session_state.selected_sv == "SV3":
              # Will only appear if it exists
            try:
                rohefaktor_lisa.addJuht(arvutustabel3, "SV3")
            except NameError:
                #st.warning("arvutustabel2 is not defined, using arvutustabel1 instead.")
                rohefaktor_lisa.addJuht(arvutustabel1, "SV1") 

    with rohe2:
        if agree:
            boonus.bonus()










