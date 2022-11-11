import streamlit as st
import streamlit.components.v1 as components

#Configuración inicial de la página
st.set_page_config(
    page_icon=":thumbs_up:",
    layout="wide"
)

st.sidebar.write(" Información sobre la cantidad de incendios forestales en la Región de Los Lagos en las temporadas 2017 a 2022.")

st.write("### Incendios forestales en la Región de Los Lagos")
st.write("En esta página web usted podrá observar la cantidad de incendios forestales ocurridos en la Región de Los Lagos durante las temporadas 2017 a 2022, dicha información fue obtenida mediante el levantamiento realizado por por equipo especializado de la Corporación Nacional Forestal (CONAF) durante dicho periodo.")
st.write("Información respecto al aeronave llegada para combatir los incendios forestales en la temporada 2021.")
st.write("Reportaje de 24 Horas, TVN")

components.html("""
    <iframe width="900" height="500" 
    src="https://www.youtube.com/embed/0TxME69JIrU" 
    title="YouTube video player" frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
""", height=520)

st.write("Durante su navegación en esta página web podrá encontrar apartados con información mediante diversos gráficos realizados especialmente para esta ocación y mediante una visualización web.")