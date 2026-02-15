# Vehicles
# Vehicle Data Visualization App

This project is a **Streamlit web application** that allows users to explore a dataset of car listings in the U.S. through **interactive histograms and scatter plots**. It leverages **Plotly** for interactive visualizations and is designed for easy exploration of key variables such as odometer readings and prices.

---

## Features

- **Histogram Generation**: Visualize the distribution of odometer readings.
- **Scatter Plot Generation**: Analyze the relationship between odometer and price.
- **Interactive Controls**: 
  - Buttons to generate plots on demand.
  - Checkboxes to dynamically display or hide visualizations.

---

## Technologies Used

- **Python 3.11**
- **Streamlit** – for web app interface
- **Pandas** – for data manipulation
- **Plotly** – for interactive charts
- **Pathlib** – for managing file paths

---

## File Structure


Vehicles/
│
├── app.py # Main Streamlit application
├── vehicles_us.csv # Dataset of car listings
└── notebooks/ # Optional Jupyter notebooks for exploration


---

## How to Run Locally

1. Clone this repository:

```bash
git clone https://github.com/<your-username>/Vehicles.git
cd Vehicles

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Install dependencies:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run app.py

The app will open in your browser, and you can interact with histograms and scatter plots.

Screenshots

Include a few screenshots of the app running here, e.g., histogram and scatter plot.

About the Dataset

The dataset vehicles_us.csv contains car listings in the U.S., including attributes such as:

odometer – distance the car has traveled (in miles)

price – listing price of the car (in USD)

This project focuses on visual exploration of these variables for insights and analysis.

Author

Juan Manuel Puentes Sayo – Biomedical Engineer & Data Enthusiast