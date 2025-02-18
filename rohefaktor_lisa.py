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
    
    data_1 = {
        "Komponendid": [
            "Täisehitatud, kõvakattega, vett mitteläbilaskvad alad.",
            "Maapinnaga ühendatud taimkattega ala.",
            "Haljastatud/looduslike kallastega vee-elupaigad ja looduslikud veekogud.",
            "Vett läbilaskvad pinnakatted ja ka sillutised.",
            "Väärtuslik kasvukohatüüp.",
        ],
        "Sisestage Ühikuid DP (m²)": st.session_state[f"{key_prefix}_data"],  # Editable column
        "Selgitus": [
        "Alad, mis ei panusta rohefaktorisse. Hoonete puhul võetakse detailplaneeringu rohefaktoris arvesse ehitusalune pind. Ehitusloa staadiumis on võimalik võtta arvesse konsoolsete osade alla jääv maapinnaga ühendatud haljastus. Boonusfaktorina võib olla võimalik kaaluda haljaskatuste/fassaadide rajamist (vt allpool).",
        "Maakatte põhifaktorina ei eristata muru/ilupeenardee/lilleniidu vms rajatud koosluste ökoloogilist kvaliteeti. Erinev rohefaktor saavutatakse samale alale täiendavate boonusfaktorite arvesse võtmise teel (vt allpool). See tähendab, et muru puhul jääb koefitsient ikka 1-ks , aga lilleniidu puhul arvutatakse boonusfaktori real sama pindala veelkord läbi faktoriga 0,4, mis summeerides annab kokku 1,4. ",
        "Elurikkust ja jätkusuutlikku sademeveekäitlust soosivad vee-elupaigad. Siin ei võeta arvesse tehislikke basseine/purskkaevusid, need arvestada kõvakattega alade hulka.",
        "Siin võetakse arvesse kõik maakattetüübid, kus <80 protsendi laotisest vett mitteläbilaskev. Arvutus ei erista sillutisi nende läbilaskevõime järgi. Ehitusloa staadiumis täpsustatakse komponenti, kusjuures võib sõltuvalt materjalivalikust koefitsient olla nii kõrgem kui madalam (0,3-0,5) ",
        "Võrdsustatakse nimetatud korra §11 lg (4) säilitamiskohustusega I-II klassi kasvukohatüübid ja III-IV väärtusklassi kasvukohatüübid. NB! Väärtusliku kasvukohatüübi esinemisalale ei rakendata boonusfaktoreid, ehk nende ulatuses ei ole lubatud vee-elupaikade rajamine, uute puude istutamine vms. Uute rohetaristu komponentide rajamine väärtuslikes elupaikades rikuks elupaiga tunnused.",
    ],
    }

    df_1 = pd.DataFrame(data_1)

    # 📌 DISPLAY FIRST TABLE (Editable)
    #col_ro, col2 = st.columns([1, 1])  # Two equal columns
    #st.title("📊 Rohefaktori Kalkulaator")

    st.subheader("🔹 Sisesta väärtused juhtotstarve")

    #col_table, col_info = st.columns([3, 1])

        # Display editable table with inline info buttons
    
    edited_df_1 = st.data_editor(
        df_1.drop(columns=["Selgitus"]),  # Hide Selgitus column from main table
        key="table_with_info",
        column_config={
            "Komponendid": st.column_config.Column("Komponendid", disabled=True, width="large"),
            "Sisestage Ühikuid DP (m²)": st.column_config.Column(
                "Sisestage Ühikuid DP (m²)", 
                required=True, 
                width="medium", 
                help="Täita tuleb ainult see veerg."
            ),
            "Info": st.column_config.Column("ℹ️ Info", disabled=True, width="small"),
        },
        hide_index=True,
    )

    # Create columns and popovers with compact buttons
    col1= st.columns(1)

    #with col1:
    with st.popover(f"ℹ️"):
        st.markdown(f"**{df_1['Komponendid'][0]}**")
        st.write(df_1["Selgitus"][0])
        st.markdown(f"**{df_1['Komponendid'][1]}**")
        st.write(df_1["Selgitus"][1])
        st.markdown(f"**{df_1['Komponendid'][2]}**")
        st.write(df_1["Selgitus"][2])
        st.markdown(f"**{df_1['Komponendid'][3]}**")
        st.write(df_1["Selgitus"][3])
        st.markdown(f"**{df_1['Komponendid'][4]}**")
        st.write(df_1["Selgitus"][4])
    

    # ✅ **Force Streamlit to immediately recognize the changes**
    updated_values = edited_df_1["Sisestage Ühikuid DP (m²)"].tolist()
    if st.session_state[f"{key_prefix}_data"] != updated_values:
        st.session_state[f"{key_prefix}_data"] = updated_values
        st.rerun()  # Force a refresh to reflect changes in the second table

    RohearvutusPohi.set_pohi_ehitatud(updated_values[0])
    RohearvutusPohi.set_pohi_ehitatud(updated_values[1])
    RohearvutusPohi.set_pohi_haljas(updated_values[2])
    RohearvutusPohi.set_pohi_vett(updated_values[3])
    RohearvutusPohi.set_pohi_vaart(updated_values[4])


    data_2 = {
        "Komponendid": [
            "Täisehitatud, kõvakattega, vett mitteläbilaskvad alad.",
            "Maapinnaga ühendatud taimkattega ala.",
            "Haljastatud/looduslike kallastega vee-elupaigad ja looduslikud veekogud.",
            "Vett läbilaskvad pinnakatted ja ka sillutised.",
            "Väärtuslik kasvukohatüüp.",
        ],
        "Ühikuid DP": st.session_state[f"{key_prefix}_data"],  # ✅ Uses latest session state values
        "Koefitsient": [0, 1, 1, 0.4, 1.8],  # Fixed values
        "RF - DP": [st.session_state[f"{key_prefix}_data"][i] * [0, 1, 1, 0.4, 1.8][i] for i in range(len(updated_values))],  # Dynamic Calculation
    }


    df_2 = pd.DataFrame(data_2)

    # Format numbers to 2 decimal places
    df_2["Koefitsient"] = df_2["Koefitsient"].round(2)
    df_2["RF - DP"] = df_2["RF - DP"].round(2)

     # 📌 SECOND TABLE (Results)
    st.write("")  # Adds a blank line
    st.write("")  # Adds another blank line

    

    st.subheader("📈 Uuendatud Arvutustabel")
    st.dataframe(df_2)

    # 📌 CALCULATE "Rohefaktor" (SUM OF ALL USER INPUTS)
    rohefaktor = edited_df_1["Sisestage Ühikuid DP (m²)"].sum() / RohearvutusPohi.get_osapindala()


     # 📌 SECOND TABLE (Results)
    st.write("")  # Adds a blank line
    st.write("")  # Adds another blank line
    st.write("")  # Adds another blank line
    st.write("")  # Adds another blank line
  


    # 📌 DISPLAY CENTERED SUMMARY SECTION
    st.markdown("<div class='summary-box'>Planeeringulahendusega kavandatud maakattetüüpide rohefaktor</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box'>{rohefaktor:.2f}</div>", unsafe_allow_html=True)


    # 📌 ADD A VERTICAL DIVIDER BETWEEN COLUMNS
    #st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
