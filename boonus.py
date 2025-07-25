# 📌 ADDITIONAL TABLES FOR THE SECOND COLUMN
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def bonus(rf, pindala, excel, count):

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


    st.subheader("Boonusfaktorid: maakate, hooned (arvutuspind kattub põhifaktori arvutuspinnaga)")
    st.divider()

    numcol1, numcol2 = st.columns(2)

    help1 = "Taimkattega ala ehitiste peal (sh nii ekstensiivsed kui intensiivsed haljaskatused). Tuleb täpsustada ehitusloa staadiumis (projekteeritud haljastuslahendusest lähtuvalt on faktor 0,2-0,5). Haljasalad maaaluste garaažide, keldrite, suurte kollektorite jms kohal. Detailplaneeringus on keskmistatud haljaskatus, ehitusloa staadiumis täpsustub."
    help2 = "Haljasfassaadid ja -piirded (lubatud max kõrgus 7 m). Ehitusloa staadiumis saab pindala täpsustada. Haljasfassaadide maksimaalseks kõrguseks arvestatakse maksimaalselt 7 m. Madalamate ehitiste (piirded, abihooned jms) puhul saab sisestada väiksema kõrgusmõõdu. Ehitusloa staadiumis on võimalik tõendada, et kõrgusmõõt on suurem."
    help3 = "Haljasaladele rajatud sademevee kohtkäitlus: so maapinnalohud (>20 cm sügavused), kuhu on kavandatud sademevee kontrollitud üleujutusalad või  immutus. Mitmekesise taimestusega viibetiigi/vihmapeenrale rakenduvad haljastuse boonusfaktorid."
    help4 = "Tehispindadele rajatud sademevee kohtkäitlus: so maapinnalohud (>20 cm sügavused), kuhu on kavandatud kontrollitud üleujutusalad (tavakasutuses mänguväljakud, spordiplatsid, parklad vms). Tehispinnad, mis toimivad osana sademevee viivitussüsteemist. Erinevate tehnoloogiliste sademeveekohtkäitluslahenduste puhul (mahutid, kasutamine tarbeveeks vms) saab siia komponendi alla määrata valgala pinna, kust tehnoloogilisse lahendusse vesi kogutakse (nt katuse pind kui sademevesi kogutakse katuselt ja kasutatakse ära tarbeveena)."
    help5 = "Tehislike jäätmaade/pruunalade asendamine rohealaga planeeringuala osad, mille puhul on haljasala kujundatud varasemast tööstusmaastikust, jääkreostuse likvideerimine (so sillutatud pinnad või reostunud pinnas vms). Siin real saab lisaboonuse selle eest, kui loodusliku ala kujundamine toimub keerulistes oludes, mis eeldab esmalt loodusliku elupaiga jaoks sobivate tingimuste loomist (so reostuse likvideerimine, ehitatud keskkonna lammutamine vms)."
    help6 = "Terviklike suurte haljasalade rajamine või alade kujundamine, mis aitavad tagada rohekoridoride sidusust (tehislike elementidega katkestamata ala, mis moodustab planeeringualast min 30%). Siin real saab lisaboonuse selle eest, kui märkimisväärne osa planeeringualast (30%) jäetakse terviklikult (so teede vms tehislike elementidega katkestamata kujul) looduslikuks."

    numberfcol1 = st.number_input("**Taimkattega ala ehitiste peal. (m²)**", value=0, help=help1)
    st.write(f"Põhifaktori koefitsent on 0.3 ja komponendi väärtus on {0.3 * numberfcol1:.1f}")
    with numcol1:
        numberfcol2 = st.number_input("**Haljasfassaadid ja -piirded (keskmine kõrgus) (m)**", value=0, help=help2)
        st.write(f"Põhifaktori koefitsent on 0.4 ja komponendi väärtus on {0.4 * numberfcol2:.1f}")
    with numcol2:
        numberfcol3 = st.number_input("**Haljasfassaadid ja -piirded (laius) (m)**", value=0, help=help2)
        st.write(f"Põhifaktori koefitsent on 0.4 ja komponendi väärtus on {0.4 * numberfcol3:.1f}")
    numberfcol4 = st.number_input("**Haljasaladele rajatud sademevee kohtkäitlus: so maapinnalohud (m²)**", value=0, help=help3)
    st.write(f"Põhifaktori koefitsent on 0.3 ja komponendi väärtus on {0.3 * numberfcol4:.1f}")
    numberfcol5 = st.number_input("**Tehispindadele rajatud sademevee kohtkäitlus. (m²)**", value=0, help= help4)
    st.write(f"Põhifaktori koefitsent on 0.3 ja komponendi väärtus on {0.3 * numberfcol5:.1f}")
    numberfcol6 = st.number_input("**Tehislike jäätmaade/pruunalade asendamine rohealaga. (m²)**", value=0, help= help5)
    st.write(f"Põhifaktori koefitsent on 0.3 ja komponendi väärtus on {0.3 * numberfcol6:.1f}")
    numberfcol7 = st.number_input("**Terviklike suurte haljasalade rajamine või alade kujundamine. (m²)**", value=0, help=help6)
    st.write(f"Põhifaktori koefitsent on 0.2 ja komponendi väärtus on {0.2 * numberfcol7:.1f}")

    excel.set_bon_haljas_korg(numberfcol2)
    excel.set_bon_haljas_lai(numberfcol3)

    excel.set_bon_taimkattega_ala(numberfcol1)

    excel.set_bon_sademevee_koht(numberfcol4)
    excel.set_bon_jäätmete(numberfcol6)
    excel.set_bon_sademevee_koht_tehis(numberfcol5)
    excel.set_bon_kujudamine(numberfcol7)



    result = 0
    if pindala > 0:
        result = float(rf) + (numberfcol1 * 0.3 + numberfcol2 * 0.4 + numberfcol3 * 0.4 + numberfcol4 * 0.3 + numberfcol5 * 0.3 + numberfcol6 * 0.3 + numberfcol7 * 0.2) / pindala

    
    # 📌 DISPLAY CENTERED SUMMARY SECTION
    st.markdown("<div class='summary-box'>Kavandatud maakasutuse ja planeeritud maakatte ökoloogilist kvaliteeti arvestav rohefaktor</div>", unsafe_allow_html=True)
    if (result >= count):
        st.markdown(f"<div class='result-box'>{result:.2f}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='result-box-red'>{result:.2f}</div>", unsafe_allow_html=True)
    
    
    #st.markdown(f"<div class='result-box'>{result:.2f}</div>", unsafe_allow_html=True)

    return result, excel