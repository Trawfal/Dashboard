import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")

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

df["Month"] = df["Start_Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Meses dos anos", df["Month"].unique())

df_filtered = df[df["Month"] == month]
df_filtered

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered, x="Start_Date", y="Total_hectares", title="")
col1.plotly_chart(fig_date)




