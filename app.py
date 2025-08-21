import streamlit as st
import pandas as pd
import plotly.express as px

# Leyendo el dataframe
df_vehicles = pd.read_csv(
    r"D:\Data\Programación\Cursos\Data_Science\TT\Sprint_7\Proyecto_Sprint_7\Vehicles_PS7\vehicles_us.csv")

# Título
st.title("EDA VEHICLES")

# Subtítulo - Selección de opciones
st.header("Seleccione el gráfico a desplegar")

# Menú desplegable para seleccionar opciones
option = st.selectbox(
    'Gráficos disponibles:',
    [
        "Gráfico de Barras: Cuota de mercado por marca",
        "Histograma: Kilometraje",
        "Gráfico de Barras: Conteo de Vehículos por Año de Manufactura",
        "Pie Chart: Distribución de Tipo de Combustible",
        "Scatter Plot: Precio vs Kilometraje (Top 3 Modelos más relevantes)"
    ]
)

# === Gráfico de Barras: Cuota de mercado por marca ===
if option == "Gráfico de Barras: Cuota de mercado por marca":

    if st.button("Desplegar"):

        vehicles = df_vehicles['model']
        vehicle_brand = vehicles.str.split().str[0]
        vehicle_brand_counts = vehicle_brand.value_counts().reset_index()

        fig = px.bar(
            vehicle_brand_counts,
            x='model',
            y='count',
            color='count',
            title='CUOTA DE MERCADO POR MARCA',
            labels={'model': 'Marca', 'count': 'Número de unidades'}
        )

        fig.update_yaxes(
            tickformat=',',
            tickprefix='',
            ticksuffix='',
            ticks='outside'
        )

        fig.show()

        st.plotly_chart(fig)

# === Histograma: Kilometraje ===
if option == "Histograma: Kilometraje":

    if st.button('Desplegar'):

        odometer_values = df_vehicles['odometer']

        fig = px.histogram(
            odometer_values,
            title='DISTRIBUCIÓN DE KILOMETRAJES',
            color_discrete_sequence=['#002535']
        )

        fig.update_xaxes(
            title='Odómetro',
            tickformat=',',
            tickprefix='',
            ticksuffix=' Km',
            ticks='outside'
        )

        fig.update_yaxes(
            title='Conteo de Vehículos'
        )

        fig.show()

        st.plotly_chart(fig)

# === Gráfico de Barras: Conteo de Vehículos por Año de Manufactura ===
if option == "Gráfico de Barras: Conteo de Vehículos por Año de Manufactura":

    if st.button('Desplegar'):

        vehicles_per_year = df_vehicles.groupby(
            'model_year').size().sort_values().reset_index(name='count')

        fig = px.bar(
            vehicles_per_year,
            x='model_year',
            y='count',
            color='count',
            title='CONTEO DE VEHÍCULOS POR AÑO DE MANUFACTURA',
            labels={'model_year': 'Año/Modelo del Vehículo',
                    'count': 'Número de vehículos'}
        )

        fig.show()

        st.plotly_chart(fig)

# === Pie Chart: Distribución de Tipo de Combustible ===
if option == "Pie Chart: Distribución de Tipo de Combustible":

    if st.button('Desplegar'):

        fuel_type_count = df_vehicles['fuel'].value_counts().reset_index()

        fig = px.pie(
            fuel_type_count,
            names='fuel',
            values='count',
            title='DISTRIBUCIÓN DEL TIPO DE COMBUSTIBLE',
            color='fuel'
        )

        fig.show()

        st.plotly_chart(fig)

# === Scatter Plot: Precio vs Kilometraje (Top 3 Modelos más relevantes) ===
if option == "Scatter Plot: Precio vs Kilometraje (Top 3 Modelos más relevantes)":

    modelo = st.radio(
        "Selecciona un Modelo:",
        [
            'Ford - F150',
            'Chevrolet Silverado 1500',
            'RAM 1500'
        ],
        index=None
    )

    # Máscaras booleanas (filtrado por Marca y Modelo)
    BM_model_f150 = df_vehicles['model'] == 'ford f-150'
    BM_model_silverado_1500 = df_vehicles['model'] == 'chevrolet silverado 1500'
    BM_model_ram_1500 = df_vehicles['model'] == 'ram 1500'

    # Datos flitrados (aplicando máscaras booleanas)
    f150_data = df_vehicles[BM_model_f150]
    silverado_1500_data = df_vehicles[BM_model_silverado_1500]
    ram_1500_data = df_vehicles[BM_model_ram_1500]

    # Ford F150
    if modelo == 'Ford - F150':

        if st.button('Desplegar', key="btn_f150"):

            # Truncando los datos para modelos mayores a 1990
            BM_model_f150_filtered = f150_data['model_year'] > 1990
            f150_data_filtered = f150_data[BM_model_f150_filtered]

            # Gráfico
            fig = px.scatter(
                f150_data_filtered,
                x='odometer',
                y='price',
                color='model_year',
                title='PRECIO vs KILOMETRAJE - FORD F-150',
                labels={'odometer': 'Kilometraje',
                        'price': 'Precio en USD', 'model_year': 'Año/Modelo'}
            )

            fig.update_xaxes(
                tickformat=',',
                tickprefix='',
                ticksuffix=' Km',
                ticks='outside'
            )

            fig.update_yaxes(
                tickformat=',',
                tickprefix='',
                ticksuffix=' USD',
                ticks='outside'
            )

            fig.show()

            st.plotly_chart(fig)

    # Chevrolet Silverado 1500
    if modelo == 'Chevrolet Silverado 1500':

        if st.button('Desplegar', key="btn_silverado"):

            # Gráfico
            fig = px.scatter(
                silverado_1500_data,
                x='odometer',
                y='price',
                color='model_year',
                title='PRECIO vs KILOMETRAJE - CHEVROLET SILVERADO 1500',
                labels={'odometer': 'Kilometraje',
                        'price': 'Precio en USD', 'model_year': 'Año/Modelo'}
            )

            fig.update_xaxes(
                tickformat=',',
                tickprefix='',
                ticksuffix=' USD',
                ticks='outside'
            )

            fig.show()

            st.plotly_chart(fig)

    # RAM 1500
    if modelo == 'RAM 1500':

        if st.button('Desplegar', key="btn_ram"):

            fig = px.scatter(
                ram_1500_data,
                x='odometer',
                y='price',
                color='model_year',
                title='PRECIO vs KILOMETRAJE - RAM 1500',
                labels={'odometer': 'Kilometraje',
                        'price': 'Precio en USD', 'model_year': 'Año/Modelo'}
            )

            fig.update_xaxes(
                tickformat=',',
                tickprefix='',
                ticksuffix=' Km',
                ticks='outside'
            )

            fig.update_yaxes(
                tickformat=',',
                tickprefix='',
                ticksuffix=' USD',
                ticks='outside'
            )

            fig.show()

            st.plotly_chart(fig)
