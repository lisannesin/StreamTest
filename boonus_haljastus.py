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


    #st.subheader("Boonusfaktorid: kavandatav haljastus")
    #st.divider()

      #with st.container(border=True):
    #st.markdown(
    #  f"<p style='font-size: 14px; font-weight: 400;'>"
    #  f"Komponendi väärtus on {0 * numberfcol1:.1f}</p>",
    #   unsafe_allow_html=True
    #)


    help1 = "Väiksekasvulise/sammasja puu istutamine: Puu või põõsas, võra läbimõõt täiskasvanuna kuni 10 meetrit, istiku kõrgus min 1 m. Sisestatakse puude arv. Arvutuses arvesse võetava vaikepindala määramise aluseks on puude kohustuslik kasvuruum lähtuvalt https://www.riigiteataja.ee/aktilisa/4290/5201/9054/Lisa2.pdf#"
    help2 = "Keskmisekasvulise puu istutamine: Puu või põõsas, võra läbimõõt täiskasvanuna 10-20 meetrit, istiku kõrgus min 1,5 m. Sisestatakse puude arv. Arvutuses arvesse võetava vaikepindala määramise aluseks on puude kohustuslik kasvuruum lähtuvalt https://www.riigiteataja.ee/aktilisa/4290/5201/9054/Lisa2.pdf#"
    help3 = "Suurekasvulise puu istutamine: Puu või põõsas, võra läbimõõt täiskasvanuna rohkem kui 20 meetrit, istiku kõrgus min 2 m. Sisestatakse puude arv. Arvutuses arvesse võetava vaikepindala määramise aluseks on puude kohustuslik kasvuruum lähtuvalt https://www.riigiteataja.ee/aktilisa/4290/5201/9054/Lisa2.pdf#"
    help4 = "Püsikute massistutus või põõsastike istutusala. Planeeringuala osad, millele on kavandatud rikkalik taimestu/põõsastikud."
    help5 = "Kohalike looduslike liikide kasvukohtade loomine (lilleniidud, nõmmeniidud, rohustud, lodud). Väärtuslike kasvukohatüüpide taastamine/kujundamine. Planeeringuala osad, kuhu on kavandatud looduslike elupaikade taastamine."

    with st.container(border=True):
        numberfcol1 = st.number_input("**Väiksekasvulise/sammasja puu istutamine (tk), koefitsent on 0.3.**", value=0, help=help1)
        st.markdown(
            f"<p style='font-size: 14px; font-weight: 400;'>"
            f"Komponendi väärtus on {0.3 * numberfcol1:.1f}</p>",
            unsafe_allow_html=True
            )

    with st.container(border=True):
        numberfcol2 = st.number_input("**Keskmisekasvulise puu istutamine (tk), koefitsent on 0.4.**", value=0, help=help2)
        st.markdown(
            f"<p style='font-size: 14px; font-weight: 400;'>"
            f"Komponendi väärtus on {0.4 * numberfcol2:.1f}</p>",
            unsafe_allow_html=True
            )

    with st.container(border=True):
        numberfcol3 = st.number_input("**Suurekasvulise puu istutamine (tk), koefitsent on 0.5.**", value=0, help=help3)
        st.markdown(
            f"<p style='font-size: 14px; font-weight: 400;'>"
            f"Komponendi väärtus on {0.5 * numberfcol3:.1f}</p>",
            unsafe_allow_html=True
            )

    with st.container(border=True):
        numberfcol4 = st.number_input("**Püsikute massistutus või põõsastike istutusala (m²), koefitsent on 0.5.**", value=0, help= help4)
        st.markdown(
            f"<p style='font-size: 14px; font-weight: 400;'>"
            f"Komponendi väärtus on {0.5 * numberfcol4:.1f}</p>",
            unsafe_allow_html=True
            )

    with st.container(border=True):
        numberfcol5 = st.number_input("**Kohalike looduslike liikide kasvukohtade loomine (m²), koefitsent on 0.4.**", value=0, help= help5)
        st.markdown(
                f"<p style='font-size: 14px; font-weight: 400;'>"
                f"Komponendi väärtus on {0.4 * numberfcol5:.1f}</p>",
                unsafe_allow_html=True
                )

    excel.set_bonH_vaike_puu(numberfcol1)
    excel.set_bonH_kesk_puu(numberfcol2)
    excel.set_bonH_suur_puu(numberfcol3)
    excel.set_bonH_massiist(numberfcol4)
    excel.set_bonH_kasvukohad(numberfcol5)
  

    result = 0
    if pindala > 0:
        result = float(rf) + (numberfcol1 * 0.3 + numberfcol2 * 0.4 + numberfcol3 * 0.5 + numberfcol4 * 0.5 + numberfcol5 * 0.4) / pindala


    # 📌 DISPLAY CENTERED = 0 SUMMARY SECTION
    #st.markdown("<div class='summary-box'>Planeeringulahenduse rohefaktor</div>", unsafe_allow_html=True)
    #if (result >= count):
    #    st.markdown(f"<div class='result-box'>{result:.2f}</div>", unsafe_allow_html=True)
    #else:
     #   st.markdown(f"<div class='result-box-red'>{result:.2f}</div>", unsafe_allow_html=True)

    summeritud = numberfcol1 * 0.3 + numberfcol2 * 0.4 + numberfcol3 * 0.5 + numberfcol4 * 0.5 + numberfcol5 * 0.4

    return result, excel, summeritud