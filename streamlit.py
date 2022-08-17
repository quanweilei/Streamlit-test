import streamlit as st
import pandas as pd


st.title("Video Game Sales Dataset")
st.image("https://www.minecraft.net/content/dam/games/minecraft/marketplace/mediablock-buzzybees.jpg")
df = pd.read_csv("vgsales.csv")
st.dataframe(df)