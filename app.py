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

    # Inicializar el estado de la sesión para los selectbox
    if 'selected_x_value' not in st.session_state:
        st.session_state.selected_x_value = None
    if 'selected_y_value' not in st.session_state:
        st.session_state.selected_y_value = None

    # Selectbox para valores únicos de las columnas seleccionadas
    unique_x_values = df[x_axis].dropna().unique()
    unique_y_values = df[y_axis].dropna().unique()

    selected_x_value = st.selectbox(f'Selecciona un valor de {x_axis}', unique_x_values, key='selected_x_value')
    selected_y_value = st.selectbox(f'Selecciona un valor de {y_axis}', unique_y_values, key='selected_y_value')

    # Filtrar el dataframe según las selecciones
    if st.session_state.selected_x_value is not None and st.session_state.selected_y_value is not None:
        filtered_df = df.loc[(df[x_axis] == st.session_state.selected_x_value) & (df[y_axis] == st.session_state.selected_y_value)]

        # Mostrar el dataframe filtrado
        st.write('Dataframe filtrado:')
        st.dataframe(filtered_df)
