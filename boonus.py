# 📌 ADDITIONAL TABLES FOR THE SECOND COLUMN
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def bonus():

    # 📌 APPLY CUSTOM CSS TO STYLE ELEMENTS
    st.markdown(
        """
        <style>
            /* Center the summary box */
            .summary-box {
                background-color: #f0f0f0;
                width: 40%;
                padding: 10px;
                border-radius: 5px;
                text-align: center;
                color: black;
                font-weight: bold;
                font-size: 18px;
                margin: 20px auto; /* Centers the div */
            }

            /* Center the result box */
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

    # 📌 FIRST TABLE (Editable Fields)
    st.subheader("🔹 Sisesta väärtused")

    data_1 = {
        "Komponendid": [
            "Taimkattega ala ehitiste peal (sh nii ekstensiivsed kui intensiivsed haljaskatused). Tuleb täpsustada ehitusloa staadiumis (projekteeritud haljastuslahendusest lähtuvalt on faktor 0,2-0,5)",
            "Haljasfassaadid ja -piirded (lubatud max kõrgus 7 m). Ehitusloa staadiumis saab pindala täpsustada",
            "Haljasaladele rajatud sademevee kohtkäitlus: so maapinnalohud (>20 cm sügavused), kuhu on kavandatud sademevee kontrollitud üleujutusalad või  immutus.",
            "Tehispindadele rajatud sademevee kohtkäitlus: so maapinnalohud (>20 cm sügavused), kuhu on kavandatud kontrollitud üleujutusalad (tavakasutuses mänguväljakud, spordiplatsid, parklad vms).",
            "Tehislike jäätmaade/pruunalade asendamine rohealaga planeeringuala osad, mille puhul on haljasala kujundatud varasemast tööstusmaastikust, jääkreostuse likvideerimine (so sillutatud pinnad või reostunud pinnas vms).",
            "Terviklike suurte haljasalade rajamine või alade kujundamine, mis aitavad tagada rohekoridoride sidusust (tehislike elementidega katkestamata ala, mis moodustab planeeringualast min 30%).",
        ],
        "Sisestage Ühikuid DP (m²)": [0, 0, 0, 0, 0, 0],  # Editable column
        "Selgitus": [
            "Haljasalad maaaluste garaažide, keldrite, suurte kollektorite jms kohal. Detailplaneeringus on keskmistatud haljaskatus, ehitusloa staadiumis täpsustub.",
            "Haljasfassaadide maksimaalseks kõrguseks arvestatakse maksimaalselt 7 m. Madalamate ehitiste (piirded, abihooned jms) puhul saab sisestada väiksema kõrgusmõõdu. Ehitusloa staadiumis on võimalik tõendada, et kõrgusmõõt on suurem.",
            "Mitmekesise taimestusega viibetiigi/vihmapeenrale rakenduvad haljastuse boonusfaktorid.",
            "Tehispinnad, mis toimivad osana sademevee viivitussüsteemist. Erinevate tehnoloogiliste sademeveekohtkäitluslahenduste puhul (mahutid, kasutamine tarbeveeks vms) saab siia komponendi alla määrata valgala pinna, kust tehnoloogilisse lahendusse vesi kogutakse (nt katuse pind kui sademevesi kogutakse katuselt ja kasutatakse ära tarbeveena).",
            "Siin real saab lisaboonuse selle eest, kui loodusliku ala kujundamine toimub keerulistes oludes, mis eeldab esmalt loodusliku elupaiga jaoks sobivate tingimuste loomist (so reostuse likvideerimine, ehitatud keskkonna lammutamine vms).",
            "Siin real saab lisaboonuse selle eest, kui märkimisväärne osa planeeringualast (30%) jäetakse terviklikult (so teede vms tehislike elementidega katkestamata kujul) looduslikuks.",
        ],
    }

    df_1 = pd.DataFrame(data_1)

    edited_df_1 = st.data_editor(
        df_1,
        column_config={
            "Komponendid": st.column_config.Column("Komponendid", disabled=True, width="large"),
            "Sisestage Ühikuid DP (m²)": st.column_config.Column("Sisestage Ühikuid DP (m²)", required=True, width="medium"),
            "Selgitus": st.column_config.Column("Komponendid", disabled=True, width="large"),
        },
        hide_index=True,
    )

    st.subheader("📈 Uuendatud Arvutustabel")
    

    data_2 = {
        "Komponendid": [
            "Taimkattega ala ehitiste peal",
            "Haljasfassaadid ja -piirded",
            "Haljasaladele rajatud sademevee kohtkäitlus (maapinnalohud)",
            "Tehispindadele rajatud sademevee kohtkäitlus",
            "Tehislike jäätmaade/pruunalade asendamine rohealaga",
            "Terviklik suur haljasalade rajamine või alade ühendamine",
        ],
        "Ühikuid DP": edited_df_1["Sisestage Ühikuid DP (m²)"],  # Updated values from first table
        "Koefitsient": [0.3, 0.4, 0.3, 0.3, 0.3, 0.2],  # Fixed values
        "RF - DP": edited_df_1["Sisestage Ühikuid DP (m²)"] * [0.3, 0.4, 0.3, 0.3, 0.3, 0.2],  # Dynamic Calculation
    }

    df_2 = pd.DataFrame(data_2)

    # Format numbers to 2 decimal places
    df_2["Koefitsient"] = df_2["Koefitsient"].round(2)
    df_2["RF - DP"] = df_2["RF - DP"].round(2)

    st.dataframe(df_2)

    # 📌 CALCULATE "Rohefaktor" (SUM OF ALL USER INPUTS)
    rohefaktor = int(edited_df_1["Sisestage Ühikuid DP (m²)"].sum())

    # 📌 DISPLAY CENTERED SUMMARY SECTION
    st.markdown("<div class='summary-box'>Kavandatud maakasutuse ja planeeritud maakatte ökoloogilist kvaliteeti arvestav rohefaktor, mis ei võta arvesse haljastuse mitmekesisust</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box'>{rohefaktor:.2f}</div>", unsafe_allow_html=True)