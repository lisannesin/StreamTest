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
import boonus_haljastus
import io
from Classes.excelClass import ExcelClass

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

#st.subheader("**Taotlusväärtuse määramine**")
#st.divider()

col1, col2 = st.columns(2)
number = 0
option_arv = 0

st.subheader("**SAMM 1 - Rohefaktori taotlusväärtuse määramine**", help = "")
st.divider()
st.subheader("**Planeeringuala andmed**")


number = st.number_input("**Detailplaneeringuala pindala. (m²)**", value = 0.0,)

class1 = TaotlusClass(number=1, pindala=number)

count = taotlusvaartus.callVaartus(class1)

#st.write(count)

arvutustabel1 = RohearvutusPohi(class1.get_pindala(), class1.get_osapindala(), class1.get_rf())


#####################################################################################################

excel = ExcelClass(number)

rf, excel = rohefaktor_lisa.addJuht(arvutustabel1, "SV1", excel)

st.divider()
#st.subheader("**Rohefaktori arvutus**")

colBon1, colBon2 = st.columns(2)

agree = st.checkbox("Boonusfaktorite arvutus")

boonusRes= 0
finalRes = 0
if agree:
    boonusRes, excel = boonus.bonus(rf, class1.get_pindala(), excel, count)

    agree2 = st.checkbox("Haljastuse rohefaktori arvutus")

    if agree2:
        finalRes, excel = boonus_haljastus.bonus(boonusRes, class1.get_pindala(), excel, count)


st.divider()
st.subheader("**Tõmba alla tulemustega Excel**", help = "")
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

        # Call your RF calculation method (if needed)
        rf_value = class1.calculate_rf(
            class1.get_number(),
            class1.get_pindala(),
            class1.get_protsent(),
            class1.get_pind(),
            class1.get_maakasutus(),
            class1.get_osapindala()
        )

        # Build DataFrame from the excel instance
        data = {
            "DP kood": user_input,
            "RF taotlusväärtus": rf_value,
            "Planeeringulahendusega kavandatud maakattetüüpide rohefaktor": round(rf, 2),
            "Kavandatud maakasutuse ja planeeritud maakatte ökoloogilist kvaliteeti arvestav rohefaktor": round(boonusRes, 2),
            "Planeeringulahenduse rohefaktor": round(finalRes, 2),
            "": "",
            "": "",
            "Detailplaneeringuala pindala (m²)": class1.get_pindala(),
            "Maakasutuse tüüp": class1.get_maakasutus(),
            "Detailplaneeringu algatamise otsusega määratud haljastuse protsent (0-100)": class1.get_protsent(),
            "Planeeringualal säilitatavate hoonete alune pind. (m²)": class1.get_pind(),
            "Täisehitatud, kõvakattega, vett mitteläbilaskvad alad. (m²)": excel.get_pohi_taisehitatud(),
            "Maapinnaga ühendatud taimkattega ala. (m²)": excel.get_pohi_yhendatud(),
            "Looduslikud veekogud. (m²)": excel.get_pohi_looduslikud_veekogud(),
            "Vett läbilaskvad pinnakatted ja ka sillutised. (m²)": excel.get_pohi_vett_labilaskvad(),
            "Väärtuslik kasvukohatüüp. (m²)": excel.get_pohi_vaart(),
            "Haljasfassaadid ja -piirded (keskmine kõrgus) (m)": excel.get_bon_haljas_korg(),
            "Haljasfassaadid ja -piirded (laius) (m)": excel.get_bon_haljas_lai(),
            "Taimkattega ala ehitiste peal. (m²)": excel.get_bon_taimkattega_ala(),
            "Haljasaladele rajatud sademevee kohtkäitlus: so maapinnalohud (m²)": excel.get_bon_sademevee_koht(),
            "Tehispindadele rajatud sademevee kohtkäitlus. (m²)": excel.get_bon_sademevee_koht_tehis(),
            "Tehislike jäätmaade/pruunalade asendamine rohealaga. (m²)": excel.get_bon_jäätmete(),
            "Terviklike suurte haljasalade rajamine või alade kujundamine. (m²)": excel.get_bon_kujudamine(),
            "Väiksekasvulise/sammasja puu istutamine. (tk)": excel.get_bonH_vaike_puu(),
            "Keskmisekasvulise puu istutamine. (tk)": excel.get_bonH_kesk_puu(),
            "Suurekasvulise puu istutamine. (tk)": excel.get_bonH_suur_puu(),
            "Püsikute massistutus või põõsastike istutusala. (m²)": excel.get_bonH_massiist(),
            "Kohalike looduslike liikide kasvukohtade loomine. (m²)": excel.get_bonH_kasvukohad()
        }
        df1 = pd.DataFrame(list(data.items()), columns=["Väli", "Väärtus"])

        # Write to Excel in memory
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            df1.to_excel(writer, sheet_name='Rohefaktor', index=False)

        buffer.seek(0)

        st.download_button(
            label="📝 Laadi Excel",
            data=buffer,
            file_name="rohefaktor_raport.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    else:
        st.write("❌ Eelnevalt täida õige DP kood")

