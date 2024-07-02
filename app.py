import pandas as pd
import streamlit as st
import plotly.express as px

# Leer el archivo CSV
df = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.title('Lista de Vehículos')

# Texto explicativo
st.write("""
### Bienvenido a la herramienta de gráficos de dispersión

Para generar un gráfico de dispersión:
1. Selecciona la variable que deseas visualizar en el eje X del gráfico.
2. Selecciona la variable que deseas visualizar en el eje Y del gráfico.
3. Presiona el botón 'Graficar' para generar el gráfico.

¡Explora los datos y descubre tendencias interesantes!
""")

# Selección de variables para el gráfico de dispersión
st.header('Generar Gráfico de Dispersión')
x_axis = st.selectbox('Selecciona la variable para el eje X', df.columns)
y_axis = st.selectbox('Selecciona la variable para el eje Y', df.columns)

# Botón para generar el gráfico
if st.button('Graficar'):
    # Agrupar los datos por las columnas seleccionadas y contar las ocurrencias
    grouped_df = df.groupby([x_axis, y_axis]).size().reset_index(name='count')
    
    # Crear el gráfico de burbujas
    fig = px.scatter(
        grouped_df,
        x=x_axis,
        y=y_axis,
        size='count',
        color='count',
        hover_name='count',
        title=f'Dispersión de {x_axis} vs {y_axis} con Tamaño de Burbujas por Cantidad'
    )
    
    # Mostrar el gráfico en la aplicación Streamlit
    st.plotly_chart(fig)
