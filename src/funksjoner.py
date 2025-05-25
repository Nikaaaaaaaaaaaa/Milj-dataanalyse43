"""Får ikke til å teste direkte fra notebook, så prøver fra her i stedenfor"""
import requests
import pandas as pd
import os
from pandasql import sqldf 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from datetime import timedelta

def load_data():
    url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
    # Denne API krever user agent, står på nettsiden
    headers = {
        "User-Agent": "Gruppe43"
        #"Id-Modified_Since": "2024-04-21"
        #Oppdater ID-midified since hver dag
    }

    params = {
        "lat": 63.4305,
        "lon": 10.3951
    }

    res = requests.get(url, headers=headers, params=params)
    data = res.json()

    timeseries = data["properties"]["timeseries"] #Gir en liste av værdata per time 

    weather_data = [
        {
            "time": entry["time"],
            "temperature": entry["data"]["instant"]["details"].get("air_temperature"),
            "humidity": entry["data"]["instant"]["details"].get("relative_humidity"),
            "wind_speed": entry["data"]["instant"]["details"].get("wind_speed"),
            "cloud_cover": entry["data"]["instant"]["details"].get("cloud_area_fraction"),
            "pressure": entry["data"]["instant"]["details"].get("air_pressure_at_sea_level"),
        }
        for entry in timeseries  #loop gjennom værmeldingen for hver time
    ]

    df = pd.DataFrame(weather_data) # Gjør om til pandas dataframe (Gjør det til en tabell)
    return df

df = load_data()

""""""
"""Forsøk på å lagre eldre data fra API-en"""


"""Forsøk på å skape manglende verdier"""
def legg_til_manglende_verdier(df_stor, min_prosent=0.01, max_prosent=0.05):
    """
    Fjerner tilfeldig prosentandel verdier fra hver 
    kolonne, (ikke 'time') for å simulere manglende data
    """
    #min/max_prosent: minimun og maksimum prosentandel av verdiene (per kolonne) som kan fjernes 
    #(default: 5% burde kanskje justeres om datasettet blir større)
    df = df_stor.copy()
    #Lager en liste over kolonner som skal påvirkes (alle unntatt 'time'):
    kolonner = [col for col in df.columns if col != "time"]

    for kol in kolonner:  #Går gjennom hver av kolonnene og legger til manglende verdier
        #Velger en tilfeldig prosentandel mellom min og maks slik at det ikke er likt for alle kolonnene:
        prosent = random.uniform(min_prosent, max_prosent) 
        antall = int(len(df) * prosent)  #Beregner hvor mange verdier som skal fjernes (f.eks. 5% av rader)
        indeks = df.sample(n=antall).index  #Velger tilfeldig hvilke rader som skal få NaN
        df.loc[indeks, kol] = np.nan #Gjør verdiene i den aktuelle kolonnen om til NaN på de valgte radene

    return df #Returner den ødelagte df med "simulert" manglende data

df_broken = legg_til_manglende_verdier(df) 


"""Oppgave 3 Databehandling"""

def rens_data(df_broken):
    """Renser manglende og ugyldige verdier"""
    df_broken = df_broken.copy()

    #Går gjennom alle kolonner unntatt 'time' 
    #og fyller inn NaN med gjennomsnittsverdi for kolonnen
    for kol in df_broken.columns:
        if kol != "time" and df_broken[kol].isnull().any():
            gjennomsnitt = df_broken[kol].mean()
            df_broken[kol] = df_broken[kol].fillna(gjennomsnitt)


    #Dette er eksempler på data rensing som ikke er helt relevante:

    #Fjerner rader med ugyldig fuktighet (over 100 eller under 0)
    df_broken = df_broken[(df_broken["humidity"] >= 0) & (df_broken["humidity"] <= 100)]

    #Erstatt ekstreme temperaturer som ikke er mulig/ gir mening med NaN
    df_broken.loc[df_broken["temperature"] < -60, "temperature"] = pd.NA
    df_broken.loc[df_broken["temperature"] > 60, "temperature"] = pd.NA

    return df_broken

def formater_data(df_broken):
    """Formaterer dataene for å gjøre dem mer strukturert og leselig"""
    df_broken = df_broken.copy()

    #Gjør 'time' til datetime
    df_broken["time"] = pd.to_datetime(df_broken["time"], errors="coerce")

    #Runder verdier for lesbarhet
    df_broken["temperature"] = df_broken["temperature"].round(1)
    df_broken["humidity"] = df_broken["humidity"].round(0)

    if "wind_speed" in df_broken.columns:
        df_broken["wind_speed"] = df_broken["wind_speed"].round(1)
        df_broken.rename(columns={"wind_speed": "wind_speed_mps"}, inplace=True)
    elif "wind_speed_mps" in df_broken.columns:
        df_broken["wind_speed_mps"] = df_broken["wind_speed_mps"].round(1)

    #Gir nye navn til kolonner om vi vil
    df_broken.rename(columns={"wind_speed": "wind_speed_mps"}, inplace=True)

    #Endre rekkefølgen på kolonnene
    kolonne_rekkefolge = ["time", "temperature", "humidity", "wind_speed_mps", "cloud_cover", "pressure"]
    df_broken = df_broken[[col for col in kolonne_rekkefolge if col in df_broken.columns]]

    return df_broken

def flagg_kuldegrader(df_broken):
    """Legger til kolonne som viser om temperaturen er under 0 grader"""
    df_broken = df_broken.copy()
    df_broken["Kuldegrader"] = df_broken["temperature"].apply(lambda t: t < 0 if pd.notnull(t) else False)
    return df_broken

def prepare_data(df_broken):
    """Kjører alle steg: viser, renser, formaterer og legger til kolonne for kuldegrader"""
    df_broken = rens_data(df_broken)
    df_broken = formater_data(df_broken)
    df_broken = flagg_kuldegrader(df_broken)
    return df_broken


df_fixed = prepare_data(df_broken)