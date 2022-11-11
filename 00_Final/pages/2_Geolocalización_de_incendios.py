import pydeck as pdk
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_icon=":thumbs_up:",
    layout="wide",
)

@st.cache
def carga_data():
    return pd.read_excel("Incendios-Forestales-Los-Lagos-2017-2022.xlsx", header=0)

st.sidebar.write(" Información sobre la cantidad de incendios forestales en la Región de Los Lagos en las temporadas 2017 a 2022.")
#se lee la info de manera óptima
incendios =  carga_data()

st.header("Desafío final")
st.info("#### Top 5 de comunas con mayor cantidad de incendios forestales entre los años 2017 y 2022")

################################################################
col_bar, col_pie, col_table = st.columns(3, gap="large")
#Agrupar los datos en base a la columna donde están las comunas
#Se gnera la serie de la agrupación usando "Size()"
group_comuna = incendios.groupby(["Comuna"]).size()
#Se ordena de mayor a menor, gracias al uso del parámetro "ascending="
group_comuna.sort_values(axis="index", ascending=False, inplace=True)
#Ya se pueden obtener los 5 primeros registros
top5=group_comuna[0:5]

##############################################################
st.info("#### Cantidad de incendios forestales por Comuna en la Región de Los Lagos")

col_sel, col_map = st.columns([1,2])

#Crear grupos por cantidad de puntos
group_15= group_comuna.apply(lambda x: x if x <= 15 else None).dropna(axis=0)
group_40= group_comuna.apply(lambda x: x if x > 15 and x <=40 else None).dropna(axis=0)
group_max= group_comuna.apply(lambda x: x if x > 40 else None).dropna(axis=0)

with col_sel:
    comunas_agrupadas = st.multiselect(
        label="Filtrar por grupos de Comuna",
        options=["Menos de 15 Puntos", "16 a 40 Puntos", "Más de 40 Puntos"],
        help="Selecciona la agrupación a mostrar",
        default=[]
    )

filtrar = []

if "Menos de 15 Puntos" in comunas_agrupadas:
    filtrar = filtrar + group_15.index.tolist()

if "16 a 40 Puntos" in comunas_agrupadas:
    filtrar = filtrar + group_40.index.tolist()

if "Más de 40 Puntos" in comunas_agrupadas:
    filtrar = filtrar + group_max.index.tolist()

#Obtener parte de la info, se crea un nuevo DataFrame
geo_puntos_comuna = incendios[ ["Temporada", "Región", "Provincia", "Comuna","Inicio", "Detección", "Extinción", "Latitud", "Longitud"]].rename(columns={
    "Inicio": "Fecha_de_inicio",
    "Detección": "Fecha_de_detección",
    "Extinción": "Fecha_de_extinción",
})
geo_puntos_comuna.dropna(subset=["Comuna"], inplace=True)
geo_data = geo_puntos_comuna
geo_data["Fecha_de_Proceso"]="08-11-2022"

#Aplicar filtro de comuna
if filtrar:
    geo_data = geo_puntos_comuna.query("Comuna == @filtrar")

#Obtener el punto promedio entre todas las georreferencias
avg_lat =np.median(geo_data["Latitud"])
avg_lng =np.median(geo_data["Longitud"])

puntos_mapa = pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
        latitude=avg_lat,
        longitude=avg_lng,
        zoom=5.2,
        min_zoom=6,
        max_zoom=15,
        pitch=10,
    ),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=geo_data,
            pickable=True,
            auto_highlight=True,
            get_position= '[Longitud, Latitud]',
            filled=True,
            opacity=1,
            radius_scale=20,
            radius_min_pixels=3,
            #radius_max_pixels=10,
            #line_idth_min_pixels=0.01,
        ),
    ],
    tooltip={
        "html": "<b>Temporada: </b> {Temporada} <br/>"
                "<b>Región: </b> {Región} <br/>"
                "<b>Provincia: </b> {Provincia} <br/>"
                "<b>Comuna: </b> {Comuna} <br/>"
                "<b>Fecha de inicio: </b> {Fecha_de_inicio} <br/>"
                "<b>Fecha de detección: </b> {Fecha_de_detección} <br/>"
                "<b>Fecha de extinción: </b> {Fecha_de_extinción} <br/>"
                "<b>Georreferencia (Lat, Lng): </b> [{Latitud}, {Longitud}] <br/>"
    }
)



with col_map:
    st.write(puntos_mapa)
