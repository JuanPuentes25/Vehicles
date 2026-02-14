# Vehicles
Visualización de datos de vehículos

Este proyecto es una aplicación sencilla creada con Streamlit que permite visualizar datos de anuncios de venta de vehículos mediante gráficos interactivos.

El objetivo principal es practicar:

Lectura de archivos CSV con Pandas

Creación de gráficos con Plotly

Uso de botones y casillas de verificación en Streamlit

Descripción del programa

La aplicación carga un archivo llamado vehicles_us.csv, que contiene información sobre vehículos, incluyendo:

Odómetro (kilometraje)

Precio

A partir de estos datos, la aplicación permite generar distintos gráficos.

Funcionalidades
1. Histograma del odómetro

Muestra la distribución del kilometraje de los vehículos.

Se puede generar usando:

Un botón

Una casilla de verificación

2. Gráfico de dispersión (odómetro vs precio)

Muestra la relación entre el kilometraje y el precio del vehículo.

También se puede generar usando:

Un botón

Una casilla de verificación

Los gráficos son interactivos y permiten explorar mejor los datos.

Tecnologías utilizadas

Python

Pandas (manejo de datos)

Streamlit (interfaz de la aplicación)

Plotly (visualización de datos)

Cómo ejecutar el programa

Asegurarse de tener instaladas las librerías necesarias:

pip install streamlit pandas plotly

Ejecutar la aplicación desde la carpeta del proyecto:

streamlit run app.py

La aplicación se abrirá automáticamente en el navegador.

Estructura del proyecto
Vehicles_pro/
│
├── app.py
├── vehicles_us.csv
└── README.md
Objetivo del proyecto

Este proyecto fue desarrollado con fines educativos para aprender a:

Visualizar datos

Crear aplicaciones interactivas simples

Trabajar con datasets reales en Python