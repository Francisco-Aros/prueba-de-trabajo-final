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

#se lee la info de manera óptima
incendios =  carga_data()

st.header("Graficos sobre la cantidad de incendios forestales en la X Región de Los Lagos")
st.info("#### Top 5 de comunas con mayor cantidad de incendios forestales entre los años 2017 y 2022")
st.sidebar.write(" Información sobre la cantidad de incendios forestales en la Región de Los Lagos en las temporadas 2017 a 2022.")

################################################################
col_bar, col_pie, col_table = st.columns(3, gap="large")
#Agrupar los datos en base a la columna donde están las comunas
#Se gnera la serie de la agrupación usando "Size()"
group_comuna = incendios.groupby(["Comuna"]).size()
#Se ordena de mayor a menor, gracias al uso del parámetro "ascending="
group_comuna.sort_values(axis="index", ascending=False, inplace=True)
#Ya se pueden obtener los 5 primeros registros
top5=group_comuna[0:5]

def formato_porciento(dato: float):
    return f"{round(dato, ndigits=2)}%"

with col_bar:
    bar= plt.figure()
    top5.plot.bar(
        title="Cantidad de Incendios por Comuna",
        label="Total de Puntos",
        xlabel="Comunas",
        ylabel="Cantidad de incendios forestales",
        color="lightblue",
        grid=True,
    ).plot()
    st.pyplot(bar)

with col_pie:
    pie = plt.figure()
    top5.plot.pie(
        y="index",
        title="Cantidad de Incendios por Comuna",
        legend=None,
        autopct=formato_porciento
    ).plot()
    st.pyplot(pie)

with col_table:
    line= plt.figure()
    top5.plot.line(
        title="Cantidad de Incendios por Comuna",
        label="Total de Puntos",
        xlabel="Comunas",
        ylabel="Cantidad de incendios forestales",
        color="lightblue",
        grid=True
    ).plot()
    st.pyplot(line)