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
import io

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

st.set_page_config(
    page_title="Rohefaktori arvutamine",
    page_icon="🍃",
    #layout="wide",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "See on Tallinna rohefaktori arvutamise kalkulaator"
    }
)

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



#st.sidebar.markdown("See siin on näide!")

##########################################################################################
#st.subheader("**Detailplaneeringu rohefaktori taotlusväärtuse määramine.**")
st.divider()
st.subheader("**1. Samm: Taotlusväärtuse määramine**")
st.divider()


col1, col2 = st.columns(2)
number = 0
option_arv = 0

    

# Initialize Streamlit columns
#col_juht1, col_juht2, col_juht3 = st.columns(3)
st.write(f"### **Juhtotstarve**")

number = st.number_input("**Kogu detailplaneeringuala pindala (m2)**", value = 0.0,)

class1 = TaotlusClass(number=1, pindala=number)


taotlusvaartus.callVaartus(class1)

#st.write(class1) 
#st.write(class1.get_osapindala())



arvutustabel1 = RohearvutusPohi(class1.get_pindala(), class1.get_osapindala(), class1.get_rf())



#####################################################################################################
st.divider()
st.subheader("**2. Samm: Rohefaktori arvutus**")

rf = 0
buffer = io.BytesIO()
user_input = 'NULL'
datatest = 'NULL'

col1, col2 = st.columns(2)

with col1:
    st.write('Sisesta DP kood:')
    user_input = st.text_input('Sisesta kood:', placeholder="Sisesta kood:", label_visibility="collapsed")

with col2:
    st.write('Tõmba alla tulemuste Excel:')

    if user_input.upper().startswith("DP") and len(user_input) == 8:
        datatest = user_input

        count = class1.calculate_rf(class1.get_number(),
					    class1.get_pindala(),
 					    class1.get_protsent(), 
					    class1.get_pind(), 
					    class1.get_maakasutus(),
                        class1.get_osapindala())

        # ✅ Create the Excel content BEFORE rendering the button
        df1 = pd.DataFrame({"DP kood": [user_input], "RF": [count]})

        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            df1.to_excel(writer, sheet_name='Sheet1', index=False)

        buffer.seek(0)

        st.download_button(
            label="📝 Laadi Excel",
            data=buffer,
            file_name="rohefaktor_raport.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        #st.write('Tõmba alla tulemuste Excel:')
        st.write("❌ Eelnevalt täida õige DP kood")



st.divider()


agree = st.checkbox("Boonusfaktorite arvutus")

rf = rohefaktor_lisa.addJuht(arvutustabel1, "SV1")

if agree:
    boonus.bonus()














