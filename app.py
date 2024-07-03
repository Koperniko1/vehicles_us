import pandas as pd
import streamlit as st
import plotly.express as px

# Leer el archivo CSV
df = pd.read_csv('vehicles_us.csv')

# Reemplazar NaN con 'No' y 1.0 con 'Sí'
df['is_4wd'] = df['is_4wd'].fillna(0).map({1.0: 'Sí', 0.0: 'No'})

# Guardar el DataFrame actualizado en el archivo CSV
df.to_csv('vehicles_us_updated.csv', index=False)

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
x_axis = st.selectbox('Selecciona la variable para el eje X', df.columns, key='x_axis')
y_axis = st.selectbox('Selecciona la variable para el eje Y', df.columns, key='y_axis')

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
        hover_name='count',
        title=f'Dispersión de {x_axis} vs {y_axis} con Tamaño de Burbujas por Cantidad'
    )
    
    # Establecer el color de las burbujas
    fig.update_traces(marker=dict(color='salmon'))
    
    # Guardar la gráfica en el estado de la sesión para que persista
    st.session_state['fig'] = fig

# Mostrar el gráfico guardado si existe en el estado de la sesión
if 'fig' in st.session_state:
    st.plotly_chart(st.session_state['fig'])

# Inicializar el estado de la sesión para los selectbox de filtrado
if 'selected_x_value' not in st.session_state:
    st.session_state.selected_x_value = None
if 'selected_y_value' not in st.session_state:
    st.session_state.selected_y_value = None

# Texto explicativo para la sección de filtrado
st.write("""
### Filtrado de Datos

Después de generar el gráfico de dispersión, puedes filtrar el dataframe según las variables seleccionadas para los ejes X y Y.

1. **Selecciona un valor del eje X**: Esto actualizará la lista de valores disponibles para el eje Y.
   
2. **Selecciona un valor del eje Y**: Esto filtrará los datos y mostrará un dataframe con los registros que coincidan con ambos valores seleccionados.

Opcional: puedes elegir las columnas que necesites del dataframe en caso de que no requieras toda la información.

Utiliza estas opciones para explorar y analizar subconjuntos específicos de los datos.
""")

# Función para ordenar valores únicos
def sort_unique_values(values):
    if pd.api.types.is_numeric_dtype(values):
        return sorted(values)
    else:
        return sorted(values, key=str)

# Selectbox para valores únicos de las columnas seleccionadas
unique_x_values = sort_unique_values(df[x_axis].dropna().unique())
selected_x_value = st.selectbox(f'Selecciona un valor de {x_axis}', unique_x_values, key='selected_x_value')

# Filtrar el dataframe según la selección del eje X para obtener valores únicos válidos para el eje Y
if selected_x_value:
    unique_y_values = sort_unique_values(df[df[x_axis] == selected_x_value][y_axis].dropna().unique())
else:
    unique_y_values = sort_unique_values(df[y_axis].dropna().unique())

selected_y_value = st.selectbox(f'Selecciona un valor de {y_axis}', unique_y_values, key='selected_y_value')

# Filtrar el dataframe según las selecciones
if selected_x_value and selected_y_value:
    filtered_df = df.loc[(df[x_axis] == selected_x_value) & (df[y_axis] == selected_y_value)]

    # Mostrar el dataframe filtrado con las columnas seleccionadas
    st.write('Dataframe filtrado:')
    columns_to_show = st.multiselect('Selecciona las columnas para visualizar', filtered_df.columns)
    if columns_to_show:
        st.dataframe(filtered_df[columns_to_show])
    else:
        st.dataframe(filtered_df)

    # Añadir sección para generar histograma
    st.write("""
    ### Generar Histograma
    
    Selecciona una columna y el número de bins para generar un histograma basado en los datos filtrados.
    """)
    
    # Selección de la columna para el histograma
    hist_column = st.selectbox('Selecciona la columna para el histograma', filtered_df.columns, key='hist_column')
    
    # Selección del número de bins
    bins = st.number_input('Número de bins', min_value=1, max_value=100, value=10, step=1, key='bins')
    
    # Botón para generar el histograma
    if st.button('Generar Histograma'):
        fig_hist = px.histogram(filtered_df, x=hist_column, nbins=bins, title=f'Histograma de {hist_column} con {bins} bins')
        
        # Establecer el color de los bins
        fig_hist.update_traces(marker=dict(color='salmon'))
        
        st.plotly_chart(fig_hist)
