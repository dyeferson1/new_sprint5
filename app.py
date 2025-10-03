import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# Resolve o caminho do CSV (funciona se app.py estiver na raiz ou em Notebooks/)
HERE = Path(__file__).resolve().parent
candidates = [
    HERE / "vehicles.csv",           # se app.py estiver na raiz
    HERE.parent / "vehicles.csv"     # se app.py estiver em Notebooks/
]
for p in candidates:
    if p.exists():
        csv_path = p
        break
else:
    st.error("Arquivo 'vehicles.csv' não encontrado. Coloque-o na raiz do projeto.")
    st.stop()

# Carrega dados
car_data = pd.read_csv(csv_path)

# UI
st.header("Dashboard de Anúncios de Veículos")
st.write(f"Fonte de dados: `{csv_path}`")

col1, col2 = st.columns(2)

with col1:
    hist_button = st.button("Criar histograma (odometer)")
with col2:
    scatter_button = st.button("Criar dispersão (odometer x price)")

if hist_button:
    st.write("Criando um histograma para a coluna **odometer**")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    st.write("Criando um gráfico de dispersão **odometer x price**")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
