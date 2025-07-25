class ExcelClass:
    def __init__(self, pindala):
        self._pindala = pindala
        self._osapindala = 0
        self._alune_pind = 0
        self._pohi_taisehitatud = 0
        self._pohi_yhendatud = 0
        self._pohi_looduslikud_veekogud = 0
        self._pohi_vett_labilaskvad = 0
        self._pohi_vaart = 0
        self._bon_haljas_korg = 0
        self._bon_haljas_lai = 0
        self._bon_taimkattega_ala = 0
        self._bon_sademevee_koht = 0
        self._bon_jäätmete = 0
        self._bon_sademevee_koht_tehis = 0
        self._bon_kujudamine = 0
        self._bonH_vaike_puu = 0
        self._bonH_kesk_puu = 0
        self._bonH_suur_puu = 0
        self._bonH_massiist = 0
        self._bonH_kasvukohad = 0

    # --- Getters ---
    def get_pindala(self):
        return self._pindala

    def get_osapindala(self):
        return self._osapindala

    def alune_pind(self):
        return self._alune_pind

    def get_pohi_taisehitatud(self):
        return self._pohi_taisehitatud

    def get_pohi_yhendatud(self):
        return self._pohi_yhendatud

    def get_pohi_looduslikud_veekogud(self):
        return self._pohi_looduslikud_veekogud

    def get_pohi_vett_labilaskvad(self):
        return self._pohi_vett_labilaskvad

    def get_pohi_vaart(self):
        return self._pohi_vaart

    def get_bon_haljas_korg(self):
        return self._bon_haljas_korg

    def get_bon_haljas_lai(self):
        return self._bon_haljas_lai

    def get_bon_taimkattega_ala(self):
        return self._bon_taimkattega_ala

    def get_bon_sademevee_koht(self):
        return self._bon_sademevee_koht

    def get_bon_jäätmete(self):
        return self._bon_jäätmete

    def get_bon_sademevee_koht_tehis(self):
        return self._bon_sademevee_koht_tehis

    def get_bon_kujudamine(self):
        return self._bon_kujudamine

    def get_bonH_vaike_puu(self):
        return self._bonH_vaike_puu

    def get_bonH_kesk_puu(self):
        return self._bonH_kesk_puu

    def get_bonH_suur_puu(self):
        return self._bonH_suur_puu

    def get_bonH_massiist(self):
        return self._bonH_massiist

    def get_bonH_kasvukohad(self):
        return self._bonH_kasvukohad

    # --- Setters ---
    def set_pindala(self, value):
        self._pindala = value

    def set_osapindala(self, value):
        self._osapindala = value

    def set_rf(self, value):
        self._alune_pind= value

    def set_pohi_taisehitatud(self, value):
        self._pohi_taisehitatud = value

    def set_pohi_yhendatud(self, value):
        self._pohi_yhendatud = value

    def set_pohi_looduslikud_veekogud(self, value):
        self._pohi_looduslikud_veekogud = value

    def set_pohi_vett_labilaskvad(self, value):
        self._pohi_vett_labilaskvad = value

    def set_pohi_vaart(self, value):
        self._pohi_vaart = value

    def set_bon_haljas_korg(self, value):
        self._bon_haljas_korg = value

    def set_bon_haljas_lai(self, value):
        self._bon_haljas_lai = value

    def set_bon_taimkattega_ala(self, value):
        self._bon_taimkattega_ala = value

    def set_bon_sademevee_koht(self, value):
        self._bon_sademevee_koht = value

    def set_bon_jäätmete(self, value):
        self._bon_jäätmete = value

    def set_bon_sademevee_koht_tehis(self, value):
        self._bon_sademevee_koht_tehis = value

    def set_bon_kujudamine(self, value):
        self._bon_kujudamine = value

    def set_bonH_vaike_puu(self, value):
        self._bonH_vaike_puu = value

    def set_bonH_kesk_puu(self, value):
        self._bonH_kesk_puu = value

    def set_bonH_suur_puu(self, value):
        self._bonH_suur_puu = value

    def set_bonH_massiist(self, value):
        self._bonH_massiist = value

    def set_bonH_kasvukohad(self, value):
        self._bonH_kasvukohad = value