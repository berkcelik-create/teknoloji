import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Gaming Gear Tracker", layout="centered")

st.title("🎮 Gaming Gear Fiyat Takipçisi")
st.write("Favori donanımlarının fiyat değişimlerini buradan izle.")

# Veriyi oku
df = pd.read_csv("data.csv")

# Grafiği çizdir
fig = px.line(df, x='Tarih', y='Fiyat', markers=True, title="Ürün Fiyat Geçmişi")
st.plotly_chart(fig)

# İstatistikler
st.metric("En Düşük Fiyat", f"{df['Fiyat'].min()} TL")
st.metric("Güncel Fiyat", f"{df['Fiyat'].iloc[-1]} TL")
