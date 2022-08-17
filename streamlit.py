import streamlit as st
import pandas as pd


st.title("Video Game Sales Dataset")
st.image("https://www.minecraft.net/content/dam/games/minecraft/marketplace/mediablock-buzzybees.jpg")
url = "https://github.com/quanweilei/Streamlit-test/blob/bd803a68a546c1c02f51f0a08fa8a2fddfdead11/vgsales.csv"
df = pd.read_csv(url, index_col = 0)
st.dataframe(df)