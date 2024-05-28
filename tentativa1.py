import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")
st.title(":orange[Incendios florestais no Mexico ]")
st.subheader("Ainda pensando no que escrever")

#Media de hectares queimado por ano
#Cidades com mais recorrencias de incendios
#Qual regiao tem mais incendios
#Duracao media dos incendios
#Vegetacao que mais propensa a incendios
#Causa dos Incendios
#Horario de comeco relacionado com a causa

df = pd.read_csv("Fires.csv", header=0, encoding='latin-1')

df["Start_Date"] = pd.to_datetime(df["Start_Date"])
df["End_Date"] = pd.to_datetime(df["End_Date"])
df["Longitude"].astype(str).astype(float)
df["Latitude"].astype(str).astype(float)

df["Year"] = df["Start_Date"].apply(lambda x: str(x.year))
df["Month"] = df["Start_Date"].apply(lambda x: str(x.month))

st.sidebar.header("Please filter here:")
year = st.sidebar.multiselect(
    "Select the year:",
    options=df["Year"].unique(),
    default= "2015"
)

month = st.sidebar.multiselect(
    "Select the month:",
    options=df["Month"].unique(),
    default= "1"
)

df_selection = df.query(
    "Year == @year & Month == @month"
)

st.dataframe(df_selection)


col1, = st.columns(1)
col2, col3 = st.columns(2)
col4, col5 = st.columns(2)

fig_date1 = px.density_mapbox(df, lat = 'Latitude', lon = 'Longitude', z = 'Total_hectares',
                        radius = 15,
                        center = dict(lat = 23.87, lon = -102.48),
                        zoom = 4,
                        height = 700,
                        color_continuous_scale=px.colors.cyclical.IceFire,
                        mapbox_style = 'carto-positron',
                        title="Heatmap of Fires"
                        )
col1.plotly_chart(fig_date1, use_container_width=True)

fig_date2 = px.bar(df_selection,
                  x="Start_Date",
                  y="Total_hectares",
                  color="Total_hectares",
                  title="Total of hectares burned"
                  )
col2.plotly_chart(fig_date2)

fig_date3 = px.bar(df_selection,
                   x="Start_Date",
                   y="Cause",
                   color="Cause",
                   title="Cause of burned hectares"
                   )
col3.plotly_chart(fig_date3)

fig_date4 = px.bar(df_selection,
                  x="Start_Date",
                  y="Total_hectares",
                  color="Total_hectares",
                  title="Total of hectares burned"
                  )
col4.plotly_chart(fig_date4)

fig_date5 = px.bar(df_selection,
                  x="Start_Date",
                  y="Total_hectares",
                  color="Total_hectares",
                  title="Total of hectares burned"
                  )
col5.plotly_chart(fig_date5)
