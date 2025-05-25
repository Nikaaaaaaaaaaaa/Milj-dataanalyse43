
import unittest
import sys
import os
import pandas as pd
from pandas.testing import assert_frame_equal

# Denne fungerer
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))
import funksjoner as fj


"""Klassen tester funksjonene i funksjoner.py filen, som er satt opp med 
oppstart og formaterings funksjoner for Miljødataanalyse_Kode"""
class TestFunctions (unittest.TestCase):
    def setUp(self):
        self.df = fj.load_data() #Original data
        self.ny_df = fj.legg_til_manglende_verdier(self.df) #data med manglende verdier
        self.renset_df = fj.rens_data(self.ny_df) #Data med fylte ut manglende verdier
        self.df_reformed = fj.formater_data(self.renset_df)
        self.df_kuldegrader = fj.flagg_kuldegrader(self.df_reformed)

    def test_legg_til_manglende_verdier(self):
        """Sjekker at originale df er IKKE lik den som har fått manglende verdier"""
        try:
            pd.testing.assert_frame_equal(self.df, self.ny_df)
        except AssertionError:
            # df er ikke like 
            pass
        else:
            # df er like
            raise AssertionError
        
    def test_legg_til_manglende_verdier_n(self):
        """Sjekker att det nå finnes manglende verdier"""
        mangler = self.ny_df.isnull().sum().sum()
        assert(mangler != 0)
    
    def test_rens_data(self):
        """Bør være true/sjekker at rens_data ikke forrandrer på data hvis det ikke er noe NaN"""
        self.df_uten_feil = fj.rens_data(self.df) #Rensing med fullstendig sf
        pd.testing.assert_frame_equal(self.df, self.df_uten_feil)

    def test_formater_data(self):
        """Dataframes skal ikke være like hverandre om formater data jorde det den skal"""
        pd.testing.assert_frame_equal(self.renset_df, self.df_reformed)

    def test_formater_data_format(self):
        """df_reformed og df_renset skal uansett fortsatt ha like mange rader og kolonner"""
        linjer_reformed = len(self.df_reformed)
        linjer_org = len(self.renset_df)
        rader_reformed = self.df_reformed.shape[1]
        rader_org = self.renset_df.shape[1]
        self.assertEqual(linjer_reformed, linjer_org)
        self.assertEqual(rader_reformed, rader_org)
    
    def test_flagg_kuldegrader(self):
        """Flagg kuldegrader legger till en kolonne, så de bør ha forskjellig mengde kolonner"""
        #Hvis failed: enten ingen kuldegrader, eller fungerer ikke.
        rader_reformed = self.df_reformed.shape[1]
        rader_kulde = self.df_kuldegrader.shape[1]
        self.assertNotEqual(rader_reformed, rader_kulde)

if __name__ == "__main__":
    unittest.main()