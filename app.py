import pandas as pd
import plotly.express as px
import streamlit as st
car_data = pd.read_csv(vehicles_us.csv') 

# --- Data Cleaning (for scatter plot specifically) ---
# Dropping rows with missing values for columns critical to the scatter plot
car_data_cleaned = car_data.dropna(subset=['odometer', 'price', 'condition', 'model_year'])

# --- Streamlit App Content ---

st.header('Análisis de Datos de Vehículos Usados') # Encabezado de la aplicación

st.write("Esta aplicación te permite explorar la distribución y las relaciones en los datos de vehículos usados.")

# --- Button for Histogram ---
st.subheader('Visualización de Distribuciones')
if st.button('Mostrar Histograma de Lectura de Odómetro', key='histogram_button'): # Added a unique key
    st.write('Generando histograma de las lecturas del odómetro...')

    fig_hist = px.histogram(
        car_data,
        x="odometer",
        color="condition",
        title="Distribución de Lecturas de Odómetro por Condición del Vehículo",
        labels={
            "odometer": "Lectura del Odómetro (millas)",
            "condition": "Condición del Vehículo"
        },
        template="plotly_white",
        nbins=50,
        hover_data={'price': True}
    )
    st.plotly_chart(fig_hist, use_container_width=True)
    st.write("El histograma muestra la frecuencia de los vehículos según su lectura de odómetro, segmentado por su condición.")

st.write("---") # Add a separator for better visual organization

# --- Button for Scatter Plot ---
st.subheader('Visualización de Relaciones')
if st.button('Mostrar Gráfico de Dispersión: Precio vs. Odómetro', key='scatter_button'): # Added a unique key
    st.write('Generando gráfico de dispersión de precio vs. lectura de odómetro...')

    fig_scatter = px.scatter(
        car_data_cleaned, # Use the cleaned data for the scatter plot
        x="odometer",
        y="price",
        color="condition",
        size="model_year",
        title="Precio vs. Lectura de Odómetro por Condición y Año del Modelo",
        labels={
            "odometer": "Lectura del Odómetro (millas)",
            "price": "Precio (USD)",
            "condition": "Condición del Vehículo",
            "model_year": "Año del Modelo"
        },
        template="plotly_white",
        opacity=0.7
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    st.write("El gráfico de dispersión muestra la relación entre el precio y la lectura del odómetro, coloreado por la condición del vehículo y con el tamaño del punto indicando el año del modelo.")

st.write("---")
st.write("¡Gracias por usar la aplicación para analizar datos de vehículos!")
