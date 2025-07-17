import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import Classes.pohiClass as RohearvutusPohi



def addJuht(RohearvutusPohi, key_prefix):

    # 📌 APPLY CUSTOM CSS TO STYLE COLUMNS AND ADD A DIVIDER
    st.markdown(
        """
        <style>

            /* Create a vertical divider */
            .divider {
                border-right: 2px solid #ccc;
                height: 100%;
                position: absolute;
                left: 50%;
                top: 0;
            }

            /* Center the summary box */
            .summary-box {
                background-color: ;
                width: 40%;
                padding: 10px;
                border-radius: 5px;
                text-align: center;
                color: black;
                font-weight: bold;
                font-size: 18px;
                margin: 20px auto; /* Centers the div */
            }

            /* Center the red result box */
            .result-box {
                background-color: #99dea9;
                width: 40%;
                padding: 10px;
                border-radius: 5px;
                text-align: center;
                color: black;
                font-weight: bold;
                font-size: 22px;
                margin: 10px auto; /* Centers the div */
            }

            /* Center the red result box */
            .result-box-red {
                background-color: #bf5461;
                width: 40%;
                padding: 10px;
                border-radius: 5px;
                text-align: center;
                color: black;
                font-weight: bold;
                font-size: 22px;
                margin: 10px auto; /* Centers the div */
            }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # 📌 CREATE TWO COLUMNS WITH A VERTICAL LINE
    #col1, col2 = st.columns([1, 1])  # Two equal columns

    #with col1:
        # 📌 DATA FOR FIRST TABLE (Editable)


    yhikud = [RohearvutusPohi.get_pohi_ehitatud(), RohearvutusPohi.get_pohi_ehitatud(), 
              RohearvutusPohi.get_pohi_haljas(), 
              RohearvutusPohi.get_pohi_vett(), RohearvutusPohi.get_pohi_vaart()]

    if f"{key_prefix}_data" not in st.session_state:
        st.session_state[f"{key_prefix}_data"] = yhikud

    # 📌 DISPLAY FIRST TABLE (Editable)
    #col_ro, col2 = st.columns([1, 1])  # Two equal columns
    #st.title("📊 Rohefaktori Kalkulaator")

    st.subheader("Sisesta väärtused juhtotstarve")
    st.write("Sisestage Ühikuid DP (m²)")

    #col_table, col_info = st.columns([3, 1])

        # Display editable table with inline info buttons

    numberfcol1 = st.number_input("**Täisehitatud, kõvakattega, vett mitteläbilaskvad alad.**", value=0, placeholder = "Sisestage Ühikuid DP (m²)", help="Täisehitatud, kõvakattega, vett mitteläbilaskvad alad. Alad, mis ei panusta rohefaktorisse. Hoonete puhul võetakse detailplaneeringu rohefaktoris arvesse ehitusalune pind. Ehitusloa staadiumis on võimalik võtta arvesse konsoolsete osade alla jääv maapinnaga ühendatud haljastus. Boonusfaktorina võib olla võimalik kaaluda haljaskatuste/fassaadide rajamist (vt allpool).")
    numberfcol2 = st.number_input("**Maapinnaga ühendatud taimkattega ala.**", value=0, placeholder = "Sisestage Ühikuid DP (m²)", help="Maakatte põhifaktorina ei eristata muru/ilupeenardee/lilleniidu vms rajatud koosluste ökoloogilist kvaliteeti. Erinev rohefaktor saavutatakse samale alale täiendavate boonusfaktorite arvesse võtmise teel (vt allpool). See tähendab, et muru puhul jääb koefitsient ikka 1-ks , aga lilleniidu puhul arvutatakse boonusfaktori real sama pindala veelkord läbi faktoriga 0,4, mis summeerides annab kokku 1,4.")
    numberfcol3 = st.number_input("**Looduslikud veekogud.**", value=0, placeholder = "Sisestage Ühikuid DP (m²)", help="Elurikkust ja jätkusuutlikku sademeveekäitlust soosivad vee-elupaigad. Siin ei võeta arvesse tehislikke basseine/purskkaevusid, need arvestada kõvakattega alade hulka.")
    numberfcol4 = st.number_input("**Vett läbilaskvad pinnakatted ja ka sillutised.**", value=0, placeholder = "Sisestage Ühikuid DP (m²)", help="Siin võetakse arvesse kõik maakattetüübid, kus <80 protsendi laotisest vett mitteläbilaskev. Arvutus ei erista sillutisi nende läbilaskevõime järgi. Ehitusloa staadiumis täpsustatakse komponenti, kusjuures võib sõltuvalt materjalivalikust koefitsient olla nii kõrgem kui madalam (0,3-0,5)")
    numberfcol5 = st.number_input("**Väärtuslik kasvukohatüüp.**", value=0, placeholder = "Sisestage Ühikuid DP (m²)", help= "Võrdsustatakse nimetatud korra §11 lg (4) säilitamiskohustusega I-II klassi kasvukohatüübid ja III-IV väärtusklassi kasvukohatüübid. NB! Väärtusliku kasvukohatüübi esinemisalale ei rakendata boonusfaktoreid, ehk nende ulatuses ei ole lubatud vee-elupaikade rajamine, uute puude istutamine vms. Uute rohetaristu komponentide rajamine väärtuslikes elupaikades rikuks elupaiga tunnused.")

    RohearvutusPohi.set_pohi_ehitatud(numberfcol1)
    RohearvutusPohi.set_pohi_ehitatud(numberfcol2)
    RohearvutusPohi.set_pohi_haljas(numberfcol3)
    RohearvutusPohi.set_pohi_vett(numberfcol4)
    RohearvutusPohi.set_pohi_vaart(numberfcol5)

    entered_values = [numberfcol1, numberfcol2, numberfcol3, numberfcol4, numberfcol5]
    koefitsient = [0, 1, 1, 0.4, 1.8]
    rf_dp = [round(entered_values[i] * koefitsient[i], 2) for i in range(5)]


        # Create table
    data_2 = {
        "Komponendid": [
            "Täisehitatud, kõvakattega, vett mitteläbilaskvad alad.",
            "Maapinnaga ühendatud taimkattega ala.",
            "Looduslikud veekogud.",
            "Vett läbilaskvad pinnakatted ja ka sillutised.",
            "Väärtuslik kasvukohatüüp.",
        ],
        "Ühikuid DP": entered_values,
        "Koefitsient": koefitsient,
        "RF - DP": rf_dp,
    }

    df_2 = pd.DataFrame(data_2)

    st.subheader("Lõplik Arvutustabel")

    # Display table
    st.dataframe(df_2)
    #st.dataframe(df_2.style.format(subset=["Ühikuid DP", "Koefitsient", "RF - DP"], formatter="{:.1f}"))

     # 📌 SECOND TABLE (Results)
    st.write("")  # Adds a blank line
    st.write("")  # Adds another blank line

    

    #st.subheader("📈 Uuendatud Arvutustabel")
    #st.dataframe(df_2)


    # 📌 CALCULATE "Rohefaktor" (SUM OF ALL USER INPUTS)
    rohefaktor = (numberfcol1+numberfcol2+numberfcol3+numberfcol4+numberfcol5) / int(RohearvutusPohi.get_osapindala())


     # 📌 SECOND TABLE (Results)
    #st.write("")  # Adds a blank line
    ##st.write("")  # Adds another blank line
    #st.write("")  # Adds another blank line
  


    # 📌 DISPLAY CENTERED SUMMARY SECTION
    st.markdown("<div class='summary-box'>Planeeringulahendusega kavandatud maakattetüüpide rohefaktor</div>", unsafe_allow_html=True)
    if (rohefaktor >= RohearvutusPohi.get_rf()):
        st.markdown(f"<div class='result-box'>{rohefaktor:.2f}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='result-box-red'>{rohefaktor:.2f}</div>", unsafe_allow_html=True)

    return rohefaktor


    # 📌 ADD A VERTICAL DIVIDER BETWEEN COLUMNS
    #st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
