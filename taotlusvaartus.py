import streamlit as st
from Classes.taotlusClass import TaotlusClass

def create_selectbox(label, options, placeholder, key):
    """
    Creates a unique selectbox for Streamlit.

    Parameters:
        label (str): The label for the selectbox.
        options (list): The options to display in the selectbox.
        placeholder (str): Placeholder text for the selectbox.
        key (str): Unique key to differentiate widgets.

    Returns:
        selected option: The user-selected option from the selectbox.
    """
    return st.selectbox(label, options, placeholder=placeholder, key=key)


# Define options for land use purposes
land_use_options = {
            "Avalikult kasutatavate- ja sotsiaalobjektide ala",
            "Eriotstarbeline ala",
            "Ettevõtlusala",
            "Garaazide ja parklate maa",
            "Kalmistute maa-ala",
            "Keskuse ala",
            "Konfliktala",
            "Korterelamute ala",
            "Lennuvälja ala",
            "Liiklusala",
            "Magistraaltänava äärne ärivöönd",
            "Pereelamute ala",
            "Riigikaitseliste ehitiste maa",
            "Roheala",
            "Sadama ala",
            "Segahoonestusala",
            "Supelranna ala",
            "Tehnoehitiste ala",
            "Tootmisala",
            "Veeala",
            "Väikeelamute ala",
        }


def create_slider(label, min_value, max_value, default_value, key):
    """
    Creates a unique slider for Streamlit.

    Parameters:
        label (str): The label for the slider.
        min_value (int): Minimum value for the slider.
        max_value (int): Maximum value for the slider.
        default_value (int): Default slider value.
        key (str): Unique key to differentiate widgets.

    Returns:
        int: The user-selected value from the slider.
    """
    return st.slider(label, min_value, max_value, default_value, key=key)

def create_number_input(label, key, value=0):
    """
    Creates a unique number input for Streamlit.

    Parameters:
        label (str): The label for the number input.
        key (str): Unique key to differentiate widgets.

    Returns:
        float: The user-entered number from the input.
    """
    return st.number_input(label, key=key, value=value)


def callVaartus(taotlusvaartus):  



    st.markdown(
        """
        <style>

            /* Center the summary box */
            .summary-box {
                background-color: ;
                width: 20%;
                padding: 10px;
                border-radius: 5px;
                text-align: center;
                color: black;
                font-size: 5px;
                margin: 20px auto; /* Centers the div */
            }

            /* Center the red result box */
            .result-box {
                background-color: #99dea9;
                width: 20%;
                padding: 10px;
                border-radius: 5px;
                text-align: center;
                color: black;
                font-size: 15px;
                margin: 5px auto; /* Centers the div */
            }

        </style>
        """,
        unsafe_allow_html=True,
    )

    

    selected_maakasutus = create_selectbox(
        label="**a)** " + "*Maakasutuse juhtotstarve*",
        options=land_use_options,
        placeholder="Valige juhtotstarve:",
        key=f"selectbox_juht{taotlusvaartus.get_number()}",
    )

    taotlusvaartus.set_maakasutus(selected_maakasutus)
    

    osapindala = create_number_input(
        label="**b)** " + "*Eraldi määratud juhtotstarbega ala osapindala  (m2)*",
        key=f"pindala{taotlusvaartus.get_number()}",
        value=200,
    )


    taotlusvaartus.set_osapindala(osapindala)

    protsent  = create_slider(
        label="**c)** " + "*Detailplaneeringu algatamise otsusega määratud haljastuse protsent (0-100)*",
        min_value=0,
        max_value=100,
        default_value=0,
        key=f"slider{taotlusvaartus.get_number()}",
    )

    taotlusvaartus.set_protsent(protsent)


    pind = create_number_input(
        label="**d)** " + "*Planeeringualal säilitatavate hoonete alune pind (m2)*",
        key=f"inopit{taotlusvaartus.get_number()}",
    )

    taotlusvaartus.set_pind(pind)

    if taotlusvaartus.get_rf() == None:
        count = 0
    else:
        count = taotlusvaartus.calculate_rf(taotlusvaartus.get_number(),
					    taotlusvaartus.get_pindala(),
 					    taotlusvaartus.get_protsent(), 
					    taotlusvaartus.get_pind(), 
					    taotlusvaartus.get_maakasutus(),
                        taotlusvaartus.get_osapindala())

    

    st.markdown(f'''
    <h4 style="color: green;">RF taotlusväärtus planeeringuala osale on <b>{count}</b></h4>
''', unsafe_allow_html=True)

    #st.markdown("<div class='summary-box'>Planeeringulahendusega kavandatud maakattetüüpide rohefaktor</div>", unsafe_allow_html=True)
    #st.markdown(f"<div class='result-box'>{count}</div>", unsafe_allow_html=True)