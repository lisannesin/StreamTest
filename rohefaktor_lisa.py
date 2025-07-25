import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import Classes.pohiClass as RohearvutusPohi



def addJuht(RohearvutusPohi, key_prefix, excel):

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



    yhikud = [RohearvutusPohi.get_pohi_ehitatud(), RohearvutusPohi.get_pohi_ehitatud(), 
              RohearvutusPohi.get_pohi_haljas(), 
              RohearvutusPohi.get_pohi_vett(), RohearvutusPohi.get_pohi_vaart()]

    if f"{key_prefix}_data" not in st.session_state:
        st.session_state[f"{key_prefix}_data"] = yhikud


    st.subheader("SAMM 2 - Rohefaktoris maakattetüüpide ja rohekomponentide arvesse võtmine")
    st.divider()
    st.subheader("Maakattetüüpide põhifaktorid")

    numberfcol1 = st.number_input("**Täisehitatud, kõvakattega, vett mitteläbilaskvad alad. (m²)**", value=0, placeholder = "Sisestage Ühikuid DP (m²)", help="Täisehitatud, kõvakattega, vett mitteläbilaskvad alad. Alad, mis ei panusta rohefaktorisse. Hoonete puhul võetakse detailplaneeringu rohefaktoris arvesse ehitusalune pind. Ehitusloa staadiumis on võimalik võtta arvesse konsoolsete osade alla jääv maapinnaga ühendatud haljastus. Boonusfaktorina võib olla võimalik kaaluda haljaskatuste/fassaadide rajamist (vt allpool).")
    st.write(f"Põhifaktori koefitsent on 0 ja komponendi väärtus on {0 * numberfcol1:.1f}")
    numberfcol2 = st.number_input("**Maapinnaga ühendatud taimkattega ala. (m²)**", value=0, placeholder = "Sisestage Ühikuid DP (m²)", help="Maakatte põhifaktorina ei eristata muru/ilupeenardee/lilleniidu vms rajatud koosluste ökoloogilist kvaliteeti. Erinev rohefaktor saavutatakse samale alale täiendavate boonusfaktorite arvesse võtmise teel (vt allpool). See tähendab, et muru puhul jääb koefitsient ikka 1-ks , aga lilleniidu puhul arvutatakse boonusfaktori real sama pindala veelkord läbi faktoriga 0,4, mis summeerides annab kokku 1,4.")
    st.write(f"Põhifaktori koefitsent on 1 ja komponendi väärtus on {1 * numberfcol2:.1f}")
    numberfcol3 = st.number_input("**Looduslikud veekogud. (m²)**", value=0, placeholder = "Sisestage Ühikuid DP (m²)", help="Elurikkust ja jätkusuutlikku sademeveekäitlust soosivad vee-elupaigad. Siin ei võeta arvesse tehislikke basseine/purskkaevusid, need arvestada kõvakattega alade hulka.")
    st.write(f"Põhifaktori koefitsent on 1 ja komponendi väärtus on {1 * numberfcol3:.1f}")
    numberfcol4 = st.number_input("**Vett läbilaskvad pinnakatted ja ka sillutised. (m²)**", value=0, placeholder = "Sisestage Ühikuid DP (m²)", help="Siin võetakse arvesse kõik maakattetüübid, kus <80 protsendi laotisest vett mitteläbilaskev. Arvutus ei erista sillutisi nende läbilaskevõime järgi. Ehitusloa staadiumis täpsustatakse komponenti, kusjuures võib sõltuvalt materjalivalikust koefitsient olla nii kõrgem kui madalam (0,3-0,5)")
    st.write(f"Põhifaktori koefitsent on 0.4 ja komponendi väärtus on {0.4 * numberfcol4:.1f}")
    numberfcol5 = st.number_input("**Väärtuslik kasvukohatüüp. (m²)**", value=0, placeholder = "Sisestage Ühikuid DP (m²)", help= "Võrdsustatakse nimetatud korra §11 lg (4) säilitamiskohustusega I-II klassi kasvukohatüübid ja III-IV väärtusklassi kasvukohatüübid. NB! Väärtusliku kasvukohatüübi esinemisalale ei rakendata boonusfaktoreid, ehk nende ulatuses ei ole lubatud vee-elupaikade rajamine, uute puude istutamine vms. Uute rohetaristu komponentide rajamine väärtuslikes elupaikades rikuks elupaiga tunnused.")
    st.write(f"Põhifaktori koefitsent on 1.8 ja komponendi väärtus on {1.8 * numberfcol5:.1f}")


    excel.set_pohi_taisehitatud(numberfcol1)
    excel.set_pohi_yhendatud(numberfcol2)
    excel.set_pohi_looduslikud_veekogud(numberfcol3)
    excel.set_pohi_vett_labilaskvad(numberfcol4)
    excel.set_pohi_vaart(numberfcol5)



    # 📌 CALCULATE "Rohefaktor" (SUM OF ALL USER INPUTS)
    if RohearvutusPohi.get_taotlusvaartus() > 0:
        rohefaktor = (numberfcol1 * 0 +numberfcol2+numberfcol3+numberfcol4 * 0.4 + numberfcol5 * 1.8) / RohearvutusPohi.get_taotlusvaartus()
    else:
        rohefaktor = 0
    
    #st.write(RohearvutusPohi.get_taotlusvaartus())


    # 📌 DISPLAY CENTERED SUMMARY SECTION
    st.markdown("<div class='summary-box'>Planeeringulahendusega kavandatud maakattetüüpide rohefaktor</div>", unsafe_allow_html=True)
    if (rohefaktor >= RohearvutusPohi.get_rf()):
        st.markdown(f"<div class='result-box'>{rohefaktor:.2f}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='result-box-red'>{rohefaktor:.2f}</div>", unsafe_allow_html=True)

    return rohefaktor, excel


