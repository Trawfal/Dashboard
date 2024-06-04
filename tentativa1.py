import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")
st.title(":orange[Incendios florestais no Mexico ]")
st.subheader("Incendios ocorridos no Mexico durantes os anos de 2015 a 2023")

#FEITO Media de hectares queimado por ano 
#Cidades com mais recorrencias de incendios
#FEITO Qual regiao tem mais incendios
#Duracao media dos incendios
#Vegetacao que mais propensa a incendios
#FEITO Causa dos Incendios
#FEITO Horario de comeco relacionado com a causa

df = pd.read_csv("Fires.csv", header=0, encoding='latin-1')

def hms_to_float(x):
  return (int(x.split(':')[0]) + int(x.split(':')[1]) / 60 + int(x.split(':')[2]) / 3600)

df['Duration'] = df['Duration'].apply(hms_to_float)
df["Start_Date"] = pd.to_datetime(df["Start_Date"])
df["End_Date"] = pd.to_datetime(df["End_Date"])
df["Longitude"].astype(str).astype(float)
df["Latitude"].astype(str).astype(float)
duration_median = df["Duration"].median()


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
col6, col7 = st.columns(2)

fig_date1 = px.density_mapbox(df,
                              lat = 'Latitude',
                              lon = 'Longitude',
                              z = 'Total_hectares',
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
                  color="Duration_days",
                  title="Total of land burned in hectares and duration of days"
                  )
col2.plotly_chart(fig_date2)

fig_date3 = px.bar(df_selection,
                   x="Start_Date",
                   y="Total_hectares",
                   color="Cause",
                   title="Cause of fires and the burnt totality"
                   )
col3.plotly_chart(fig_date3)

fig_date4 = px.pie(df_selection,
                  values ="Duration",
                  names ="Region",
                  title="Duration of wildfires based on region"
                  )
col4.plotly_chart(fig_date4)

df['Start_Date'] = df['Start_Date'].count()

fig_date5 = px.line (df_selection,
                  x='Start_Date',
                  title="Totality of unique fires across the years"
                  )
col5.plotly_chart(fig_date5)

fig_date6 = px.sunburst(df_selection,
                    path=["Region", "State"],
                    values="Total_hectares",
                    title="Cause of fires and the Region with most incidents"
                    )
col6.plotly_chart(fig_date6)
