import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")
st.title("Dashboard sobre Incendios florestais no Mexico")

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

df["Month"] = df["Start_Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Meses dos anos", df["Month"].unique())

df_filtered = df[df["Month"] == month]
df_filtered

col1, col2 = st.columns(2)
col3, = st.columns(1)

fig_date = px.bar(df_filtered,
                  x="Start_Date",
                  y="Total_hectares",
                  color="Total_hectares",
                  title="Total of hectares burned"
                  )
col1.plotly_chart(fig_date)

fig_date2 = px.bar(df_filtered,
                   x="Start_Date",
                   y="Cause",
                   color="Cause",
                   title="Cause of burned hectares"
                   )
col2.plotly_chart(fig_date2)

fig_date3 = px.density_mapbox(df, lat = 'Latitude', lon = 'Longitude', z = 'Total_hectares',
                        radius = 15,
                        center = dict(lat = 23.87, lon = -102.48),
                        zoom = 4,
                        color_continuous_scale=px.colors.cyclical.IceFire,
                        mapbox_style = 'carto-positron',
                        title="Heatmap of Fires"
                        )
col3.plotly_chart(fig_date3, use_container_width=True)
