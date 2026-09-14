import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Mercado de vehículos ligeros en México (AMDA, agosto 2026)")


# Igual que en la app de pases: una función que lee los datos una sola vez
@st.cache_data
def cargar_datos():
    ventas = pd.read_csv("datos/ventas_mensuales_2008_2026.csv")
    segmentos = pd.read_csv("datos/segmentos_agosto_2012_2026.csv")
    return ventas, segmentos


ventas, segmentos = cargar_datos()

# ---- Parte 1: elegir un año con un slider (como el slider de minuto) ----
anio = st.slider("Año", 2008, 2026, 2026)
datos = ventas[ventas["anio"] == anio]
st.write(f"Ventas de {anio}: {int(datos['unidades'].sum()):,} unidades")
st.dataframe(datos[["mes", "unidades"]], hide_index=True)

# TODO (equipo): aquí va la gráfica 2 del cuaderno, este año contra el anterior.
# fig, ax = plt.subplots()
# ...
# st.pyplot(fig)

# ---- Parte 2: elegir un segmento con st.selectbox ----
# TODO (equipo): st.selectbox("Segmento", [...]) y la serie de agosto de ese segmento.
