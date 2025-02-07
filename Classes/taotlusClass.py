import streamlit as st

class TaotlusClass:
    def __init__(self, number, pindala):
        self._number = number  # Unique ID or reference number
        self._pindala = pindala  # Total area
        self._maakasutus = 0  # Land use type
        self._osapindala = 0  # Partial area
        self._protsent = 0  # Percentage for calculation
        self._pind = 0  # Specific area for RF calculation
        self._rf = 0  # Rohefaktor value

    # ✅ Getters
    def get_number(self):
        return self._number

    def get_pindala(self):
        return self._pindala

    def get_maakasutus(self):
        return self._maakasutus

    def get_osapindala(self):
        return self._osapindala

    def get_protsent(self):
        return self._protsent

    def get_pind(self):
        return self._pind

    def get_rf(self):
        return self._rf

    # ✅ Setters
    def set_number(self, value):
        self._number = value

    def set_pindala(self, value):
        self._pindala = value

    def set_maakasutus(self, value):
        self._maakasutus = value

    def set_osapindala(self, value):
        self._osapindala = value

    def set_protsent(self, value):
        self._protsent = value

    def set_pind(self, value):
        self._pind = value

    def set_rf(self, value):
        self._rf = value

    def calculate_rf(self, B5, B4, B10, B11, B8):
        """
        Calculate RF taotlusväärtus based on the given formula.
        """

        # Convert inputs to float
        B10 = float(B10)  # Planeeringualal säilitatavate hoonete alune pind (m²)
        #B8 = str(B8)  # Convert to string for lookup
        B5 = float(B5)  # Planeeringualal kavandatud erinevate juhtotstarvete arv
        B4 = float(B4)  # Kogu detailplaneeringuala pindala (m²)
        B11 = float(B11) / 100  # Convert percentage to decimal

        # Lookup dictionary for "Sisendid"
        sisendid_lookup = {
            "Avalikult kasutatavate- ja sotsiaalobjektide ala": 0.3,
            "Eriotstarbeline ala": 0.05,
            "Ettevõtlusala": 0.2,
            "Garaazide ja parklate maa": 0.2,
            "Kalmistute maa-ala": 0.4,
            "Keskuse ala": 0.2,
            "Konfliktala": 0,
            "Korterelamute ala": 0.3,
            "Lennuvälja ala": 0,
            "Liiklusala": 0,
            "Magistraaltänava äärne ärivöönd": 0.15,
            "Pereelamute ala": 0.3,
            "Riigikaitseliste ehitiste maa": 0.1,
            "Roheala": 0.4,
            "Sadama ala": 0.1,
            "Segahoonestusala": 0.2,
            "Supelranna ala": 0.4,
            "Tehnoehitiste ala": 0.1,
            "Tootmisala": 0.1,
            "Veeala": 0.4,
            "Väikeelamute ala": 0.3,
        }

        # Retrieve the lookup value
        lookup_value = sisendid_lookup.get(B8, 0)  # Default to 0 if not found

        # Determine the denominator
        denominator = B4 if B5 == 1 else 200  # 200 used as default if multiple land uses

        # Apply calculation formula
        RF_taotlusvaartus = (B10 + lookup_value - (B11 / denominator) * lookup_value) if denominator != 0 else 0

        return round(RF_taotlusvaartus, 2)  # Round for better readability


    # ✅ Display information
    def __str__(self):
        return (f"TaotlusClass(Number: {self._number}, Maakasutus: {self._maakasutus}, "
                f"Pindala: {self._pindala}, Osapindala: {self._osapindala}, "
                f"Protsent: {self._protsent}, Pind: {self._pind}, RF: {self._rf})")

