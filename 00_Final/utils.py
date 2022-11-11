import streamlit as st
import pandas as pd
import os
import requests
import json
from dotenv import load_dotenv


load_dotenv()
#Leer api key 
datos_clima = os.getenv("API_KEY","123API")
#Definir lugar de consulta
ubicacion = "Puerto Montt, CL"
#Crear conexión a la API
URL = f"https://api.openweathermap.org/data/2.5/weather?q={ubicacion}&appid={datos_clima}"
datos = requests.get(URL)
print (datos)
datos_json = datos.json()

# Se crea lista de horarios de funcionamiento
# esta información puede venir desde otro Excel, CSV o API

clima = [
  
  "No Data",
]


def asigna_clima(data):
  comuna=data["Comuna"]
  latitud=data["Latitud"]

  if(latitud < -33.49):
    return clima[5]
  elif(comuna=="" and latitud < -33.51):
    return clima[0]
  elif(comuna==""):
    return clima[1]
  elif(comuna==""):
    return clima[2]
  elif(comuna==""):
    return clima[3]
  else:
    return clima[4]


@st.cache
def carga_data():
    return pd.read_excel("Incendios-Forestales-Los-Lagos-2017-2022.xlsx", header=0)

#se lee la info de manera óptima
incendios =  carga_data()
incendios["Fecha_de_Proceso"]="08-11-2022"
incendios["Clima"]=""

print(incendios)

  #Obtener parte de la info, se crea un nuevo DataFrame
geo_puntos_comuna = incendios[ ["Temporada", "Región", "Provincia", "Comuna","Inicio", "Detección", "Extinción", "Latitud", "Longitud", "Fecha_de_Proceso", "Clima"]].rename(columns={
    "Inicio": "Fecha_de_inicio",
    "Detección": "Fecha_de_detección",
    "Extinción": "Fecha_de_extinción",
})



geo_puntos_comuna.to_csv("datos_incendios.csv", encoding="utf-8")
geo_puntos_comuna.to_excel("datos_incendios.xlsx")
