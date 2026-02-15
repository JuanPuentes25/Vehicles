import pandas as pd
import streamlit as st
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go

car_data = pd.read_csv(r'C:\Users\Juan\Vehicles_pro\Vehicles\vehicles_us.csv')

st.header("Generación de un histograma")
# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

st.header("Generación de un gráfico de dispersión")

scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Creación de un gráfico de dispersión entre el odómetro y el precio")

    # Crear un scatter plot utilizando plotly.graph_objects
# Se crea una figura vacía y luego se añade un rastro de scatter
    fig1 = go.Figure(
        data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

# Opcional: Puedes añadir un título al gráfico si lo deseas
    fig1.update_layout(title_text='Relación entre Odómetro y Precio')

    st.plotly_chart(fig1, use_container_widght=True)


st.header("Histograma con casilla de verificación")
# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

    fig2 = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig2.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig2, use_container_width=True)

st.header("Gráfico de dispersión con casilla de verificación")
# crear una casilla de verificación
build_scatterplot = st.checkbox('Construir un gráfico de dispersión')

if build_scatterplot:  # si la casilla de verificación está seleccionada
    st.write('Construir un gráfico de dispersión  entre el odómetro y el precio')
# Crear un scatter plot utilizando plotly.graph_objects
# Se crea una figura vacía y luego se añade un rastro de scatter
    fig3 = go.Figure(
        data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

# Opcional: Puedes añadir un título al gráfico si lo deseas
    fig3.update_layout(title_text='Relación entre Odómetro y Precio')

    st.plotly_chart(fig3, use_container_widght=True)
