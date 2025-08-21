# Vehicles_PS7
Proyecto de práctica, desarrollo App Web

## Descripción del Proyecto

Este proyecto tiene como objetivo explorar y visualizar datos de vehículos disponibles en el mercado estadounidense utilizando un enfoque de **Exploratory Data Analysis (EDA)**. La aplicación web permite interactuar de manera sencilla con los datos y generar gráficos informativos para comprender la distribución de precios, kilometraje, marcas, tipos de combustible y otros atributos relevantes de los vehículos.

## Funcionalidad de la Aplicación Web

La app fue desarrollada con **Streamlit** y utiliza **Plotly** para los gráficos interactivos. Permite al usuario seleccionar y desplegar distintos tipos de visualizaciones a través de un menú desplegable y botones de acción:

* **Gráfico de Barras: Cuota de mercado por marca**
  Muestra la distribución de vehículos por marca, permitiendo identificar las marcas con mayor presencia en el dataset.

* **Histograma: Kilometraje (Odometer)**
  Permite analizar la distribución del kilometraje de los vehículos y detectar posibles valores atípicos o tendencias.

* **Gráfico de Barras: Conteo de Vehículos por Año de Manufactura**
  Presenta el número de vehículos disponibles por año de fabricación, mostrando tendencias temporales en los datos.

* **Pie Chart: Distribución de Tipo de Combustible**
  Visualiza la proporción de vehículos según su tipo de combustible.

* **Scatter Plot: Precio vs Kilometraje (Top 3 Modelos más relevantes)**
  Permite explorar la relación entre precio y kilometraje para los modelos más representativos (Ford F-150, Chevrolet Silverado 1500 y RAM 1500). El usuario puede seleccionar cuál modelo desea visualizar mediante checkboxes.

## Estructura de la App

```app.py
├── Importación de librerías
│   ├── streamlit as st
│   ├── pandas as pd
│   └── plotly.express as px
│
├── Lectura del dataset
│   └── df_vehicles = pd.read_csv("vehicles_us.csv")
│
├── Encabezados de la app
│   ├── st.title("EDA VEHICLES")
│   └── st.header("Seleccione el gráfico a desplegar")
│
├── Menú desplegable (st.selectbox)
│   ├── "Gráfico de Barras: Cuota de mercado por marca"
│   │     └── if st.button("Desplegar")
│   │           └── px.bar(...) → st.plotly_chart(fig)
│   │
│   ├── "Histograma: Kilometraje"
│   │     └── if st.button("Desplegar")
│   │           └── px.histogram(...) → st.plotly_chart(fig)
│   │
│   ├── "Gráfico de Barras: Conteo de Vehículos por Año de Manufactura"
│   │     └── if st.button("Desplegar")
│   │           └── px.bar(...) → st.plotly_chart(fig)
│   │
│   ├── "Pie Chart: Distribución de Tipo de Combustible"
│   │     └── if st.button("Desplegar")
│   │           └── px.pie(...) → st.plotly_chart(fig)
│   │
│   └── "Scatter Plot: Precio vs Kilometraje (Top 3 Modelos más relevantes)"
│         ├── Definición de máscaras booleanas
│         ├── Subsets de datos: f150, silverado, ram
│         │
│         ├── st.checkbox("Ford F-150")
│         │     └── if st.button("Desplegar", key="btn_f150")
│         │           └── px.scatter(...) → st.plotly_chart(fig)
│         │
│         ├── st.checkbox("Chevrolet Silverado 1500")
│         │     └── if st.button("Desplegar", key="btn_silverado")
│         │           └── px.scatter(...) → st.plotly_chart(fig)
│         │
│         └── st.checkbox("RAM 1500")
│               └── if st.button("Desplegar", key="btn_ram")
│                     └── px.scatter(...) → st.plotly_chart(fig)
```
