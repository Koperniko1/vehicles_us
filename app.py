import pandas as pd
import streamlit as st
import plotly.express as px

# Leer el archivo CSV
df = pd.read_csv('vehicles_us.csv')

# Mostrar el encabezado del DataFrame en la consola (opcional)
print(df.head())

# Título de la aplicación
st.title('Lista de Vehículos')

# Mostrar el DataFrame en la aplicación
st.write(df)

# Selección de variables para el gráfico de dispersión
st.header('Generar Gráfico de Dispersión')
x_axis = st.selectbox('Selecciona la variable para el eje X', df.columns)
y_axis = st.selectbox('Selecciona la variable para el eje Y', df.columns)

# Botón para generar el gráfico
if st.button('Graficar'):
    fig = px.scatter(df, x=x_axis, y=y_axis, title=f'Dispersión de {x_axis} vs {y_axis}')
    st.plotly_chart(fig)
