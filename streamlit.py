import streamlit as st
import pandas as pd

st.title("Video Game Sales Dataset")
st.image("https://www.minecraft.net/content/dam/games/minecraft/marketplace/mediablock-buzzybees.jpg")
df = pd.read_csv("vgsales.csv", index_col = 0)
sf = df

filter = st.text_input("Filter by Platform")

input = st.text_input("Search for Game")
if df['Name'].isin([input]).empty == False and len(input) != 0:
    st.table(df.loc[df['Name'].str.contains(input, case = False)])

table = st.radio('Display Table', ["yes", "no"])
if table == 'yes':
    st.dataframe(sf, 100000, 500)
