import streamlit as st
import streamlit.components.v1 as components

st.write("## Visualizaciones de Datos Geográficos en Internet")

components.html("""
<div style="background: white;border-radius: 5px;padding: 10px 25px;">
  <h3>
    Creado para el curso de Visualizaciones de Datos Geográficos en Internet
  </h3>
  <p>
    Creado por: <b>Francisco Javier Aros Muñoz</b>
                <p>Geógrafo
                
                 <p> Magister en Planificación y Gestión Territorial
                 <p> Valdivia
                 <p> Contacto: franciscoarosmunoz@gmail.com
  <p>
</div>
""",width=720, height=230)

st.sidebar.write(" Información sobre la cantidad de incendios forestales en la Región de Los Lagos en las temporadas 2017 a 2022.")

