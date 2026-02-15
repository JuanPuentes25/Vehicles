import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from pathlib import Path

# Carpeta donde está app.py
BASE_DIR = Path(__file__).parent

# CSV en la misma carpeta
csv_path = BASE_DIR / 'vehicles_us.csv'

# Leer CSV
car_data = pd.read_csv(csv_path)

# ----------------------------
# Histograma con botón
# ----------------------------
st.header("Generación de un histograma")
hist_button = st.button('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# Scatter plot con botón
# ----------------------------
st.header("Generación de un gráfico de dispersión")
scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Creación de un gráfico de dispersión entre el odómetro y el precio")

    fig1 = go.Figure(
        data=[go.Scatter(x=car_data['odometer'],
                         y=car_data['price'], mode='markers')]
    )
    fig1.update_layout(title_text='Relación entre Odómetro y Precio')
    st.plotly_chart(fig1, use_container_width=True)

# ----------------------------
# Histograma con checkbox
# ----------------------------
st.header("Histograma con casilla de verificación")
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Construir un histograma para la columna odómetro')

    fig2 = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig2.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig2, use_container_width=True)

# ----------------------------
# Scatter plot con checkbox
# ----------------------------
st.header("Gráfico de dispersión con casilla de verificación")
build_scatterplot = st.checkbox('Construir un gráfico de dispersión')

if build_scatterplot:
    st.write('Construir un gráfico de dispersión entre el odómetro y el precio')

    fig3 = go.Figure(
        data=[go.Scatter(x=car_data['odometer'],
                         y=car_data['price'], mode='markers')]
    )
    fig3.update_layout(title_text='Relación entre Odómetro y Precio')
    st.plotly_chart(fig3, use_container_width=True)
