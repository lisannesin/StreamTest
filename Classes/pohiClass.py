import streamlit as st

# MyClass gets redefined every time app.py reruns
class RohearvutusPohi:
    def __init__(self, taotlusvaartus, osapindala):
        self._taotlusvaartus = taotlusvaartus
        self._osapindala = osapindala
        self._pohi_ehitatud = 0
        self._pohi_maapinnaga = 0
        self._pohi_haljas = 0
        self._pohi_vett = 0
        self._pohi_vaart = 0

    # Getters
    def get_taotlusvaartus(self):
        return self._taotlusvaartus

    def get_osapindala(self):
        return self._osapindala

    def get_pohi_ehitatud(self):
        return self._pohi_ehitatud

    def get_pohi_maapinnaga(self):
        return self._pohi_maapinnaga

    def get_pohi_haljas(self):
        return self._pohi_haljas

    def get_pohi_vett(self):
        return self._pohi_vett

    def get_pohi_vaart(self):
        return self._pohi_vaart

    # Setters
    def set_taotlusvaartus(self, value):
        self._taotlusvaartus = value

    def set_osapindala(self, value):
        self._osapindala = value

    def set_pohi_ehitatud(self, value):
        self._pohi_ehitatud = value

    def set_pohi_maapinnaga(self, value):
        self._pohi_maapinnaga = value

    def set_pohi_haljas(self, value):
        self._pohi_haljas = value

    def set_pohi_vett(self, value):
        self._pohi_vett = value

    def set_pohi_vaart(self, value):
        self._pohi_vaart = value
