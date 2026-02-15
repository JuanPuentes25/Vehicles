from pathlib import Path
import plotly.graph_objects as go
import streamlit as st
iimport pandas as pd

# ----------------------------
# Load CSV using a relative path
# ----------------------------
BASE_DIR = Path(__file__).parent  # Folder where app.py is located
csv_path = BASE_DIR / 'vehicles_us.csv'

# Read CSV
car_data = pd.read_csv(csv_path)

# ----------------------------
# Histogram with button
# ----------------------------
st.header("Histogram Generation")
hist_button = st.button('Build Histogram')

if hist_button:
    st.write('Creating a histogram for the car listings dataset')

    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Odometer Distribution')
    st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# Scatter plot with button
# ----------------------------
st.header("Scatter Plot Generation")
scatter_button = st.button("Build Scatter Plot")

if scatter_button:
    st.write("Creating a scatter plot between odometer and price")

    fig1 = go.Figure(
        data=[go.Scatter(x=car_data['odometer'],
                         y=car_data['price'], mode='markers')]
    )
    fig1.update_layout(title_text='Odometer vs. Price')
    st.plotly_chart(fig1, use_container_width=True)

# ----------------------------
# Histogram with checkbox
# ----------------------------
st.header("Histogram with Checkbox")
build_histogram = st.checkbox('Build a Histogram')

if build_histogram:
    st.write('Building a histogram for the odometer column')

    fig2 = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig2.update_layout(title_text='Odometer Distribution')
    st.plotly_chart(fig2, use_container_width=True)

# ----------------------------
# Scatter plot with checkbox
# ----------------------------
st.header("Scatter Plot with Checkbox")
build_scatterplot = st.checkbox('Build a Scatter Plot')

if build_scatterplot:
    st.write('Building a scatter plot between odometer and price')

    fig3 = go.Figure(
        data=[go.Scatter(x=car_data['odometer'],
                         y=car_data['price'], mode='markers')]
    )
    fig3.update_layout(title_text='Odometer vs. Price')
    st.plotly_chart(fig3, use_container_width=True)
