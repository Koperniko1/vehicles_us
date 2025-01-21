# Herramienta de Análisis de Datos con Streamlit y Plotly

Esta aplicación web permite explorar y visualizar datos de vehículos utilizando Streamlit y Plotly. Puedes generar gráficos de dispersión interactivos, filtrar datos y realizar análisis detallados de manera sencilla e intuitiva.

## Ejecuta la Aplicación en Línea

Puedes probar la aplicación directamente desde tu navegador sin necesidad de instalar nada: [Vehicles US App](https://vehicles-us-wnm9.onrender.com).

---

## Inspiración del Tema

El diseño y aspecto visual de esta aplicación están inspirados en una aplicación de Streamlit que encontré alojada en [este enlace](https://app-theme-editor-curuunml4o9.streamlit.app/). Agradezco a sus creadores por proporcionar una fuente de inspiración para mejorar la experiencia de usuario de esta herramienta.

## Funcionalidades

- **Gráficos de Dispersión Interactivos:** Visualiza relaciones entre variables seleccionadas mediante gráficos de burbujas.
- **Filtrado de Datos:** Selecciona valores para los ejes X e Y y filtra el dataset para explorar subconjuntos específicos.
- **Histogramas Personalizables:** Genera histogramas basados en datos filtrados con opciones para ajustar el número de bins.

---

## Uso

1. **Selecciona Variables:** Elige las variables para los ejes X e Y y presiona "Graficar" para generar un gráfico de dispersión.
2. **Filtrado de Datos:** Una vez generado el gráfico, selecciona valores para los ejes X e Y para filtrar el dataset y explorar datos específicos.
3. **Exploración Adicional:** Visualiza el dataframe filtrado y genera histogramas para un análisis más profundo.

---

## Instalación Local

Si prefieres ejecutar la aplicación localmente, sigue estos pasos:

1. Asegúrate de tener [Python](https://www.python.org/) instalado en tu sistema.
2. Clona este repositorio:

```bash
git clone https://github.com/Koperniko1/vehicles_us.git
```

3. Navega al directorio del proyecto:
```bash
cd vehicles_us
```

4. Instala las dependencias requeridas:
```bash
pip install -r requirements.txt
```

5. Ejecuta la aplicación:
```bash
streamlit run app.py
```
