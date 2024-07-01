import pandas as pd
import streamlit as st  # Importa streamlit como st

# Leer el archivo CSV
df = pd.read_csv('vehicles_us.csv')

# Mostrar el encabezado del DataFrame en la consola (opcional)
print(df.head())

# Título de la aplicación
st.title('Lista de Vehículos')

# Mostrar el DataFrame en la aplicación
st.write(df)
