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

st.subheader("**Detailplaneeringu rohefaktori taotlusväärtuse leidmine**", help = "")

st.subheader("**Planeeringuala andmed**")
st.divider()

number = st.number_input("**Detailplaneeringuala pindala. (m²)**", value = 0.0,)

class1 = TaotlusClass(number=1, pindala=number)

count = taotlusvaartus.callVaartus(class1)

#st.write(count)

arvutustabel1 = RohearvutusPohi(class1.get_pindala(), class1.get_osapindala(), class1.get_rf())



#st.divider()


#####################################################################################################
st.divider()
excel = ExcelClass(number)

st.subheader("Maakattetüüpide ja rohekomponentide arvesse võtmine")

st.divider()

with st.expander("**Maakattetüüpide põhifaktorid**"):

    rf, excel, summa1 = rohefaktor_lisa.addJuht(arvutustabel1, "SV1", excel)


#st.subheader("**Rohefaktori arvutus**")

#colBon1, colBon2 = st.columns(2)

#agree = st.checkbox("Boonusfaktorite arvutus")

boonusRes= 0
finalRes = 0
with st.expander("**Boonusfaktorid: rohetaristu (vabatahtlik)**"):
    boonusRes, excel, summa2 = boonus.bonus(rf, class1.get_pindala(), excel, count)

   #agree2 = st.checkbox("Haljastuse rohefaktori arvutus")

with st.expander("**Boonusfaktorid: haljastus (vabatahtlik)**"):
    finalRes, excel, summa3 = boonus_haljastus.bonus(boonusRes, class1.get_pindala(), excel, count)

final_sum = summa1 + summa2 + summa3
st.markdown(f'''<h5 style="color: green;">ROHEKOMPONENTIDE SUMMEERITUD VÄÄRTUS <b>{final_sum:.2f}</b></h4>''', unsafe_allow_html=True)
st.divider()

with st.container(border=True):
    st.markdown(f'''<h5 style="color: green;">ROHEFAKTORI TAOTLUSVÄÄTUS <b>{count}</b></h4>''', unsafe_allow_html=True)
    if number == 0:
        st.markdown(f'''<h5 style="color: green;">ROHEFAKTORI ARVUTATUD VÄÄRTUS <b>{0}</b></h4>''', unsafe_allow_html=True)
    elif final_sum/number >= count:
        st.markdown(f'''<h5 style="color: green;">ROHEFAKTORI ARVUTATUD VÄÄRTUS <b>{final_sum/number:.2f}</b></h4>''', unsafe_allow_html=True)
    else:
        st.markdown(f'''<h5 style="color: red;">ROHEFAKTORI ARVUTATUD VÄÄRTUS <b>{final_sum/number:.2f}</b></h4>''', unsafe_allow_html=True)

st.divider()

st.subheader("**Salvesta tulemused faili (.xlsx)**", help = "")
buffer = io.BytesIO()
user_input = 'NULL'
datatest = 'NULL'

#col1, col2 = st.columns(2)


#with col1:
#    st.write('Sisesta DP kood:')
#    user_input = st.text_input('Sisesta kood:', placeholder="Sisesta kood:", label_visibility="collapsed")

#with col2:
#    st.write('Tõmba alla tulemuste Excel:')

#    if user_input.upper().startswith("DP") and len(user_input) == 8:
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

if number != 0:
    arvutatud = round(final_sum / number, 2)
else: 
    arvutatud = 0

# Build DataFrame from the excel instance
data = {
    #"DP kood": user_input,
    "ROHEFAKTORI TAOTLUSVÄÄTUS": count,
    "ROHEFAKTORI ARVUTATUD VÄÄRTUS": arvutatud,
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
    label="📝 Salvesta fail",
    data=buffer,
    file_name="rohefaktor_raport.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

    #else:
    #    st.write("❌ Eelnevalt täida õige DP kood")

