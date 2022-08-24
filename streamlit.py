import streamlit as st
import pandas as pd

st.title("Video Game Sales Dataset")
st.image("https://www.minecraft.net/content/dam/games/minecraft/marketplace/mediablock-buzzybees.jpg")
df = pd.read_csv("vgsales.csv", index_col = 0)

sf = df



input = st.text_input("Search for Game")
if df['Name'].isin([input]).empty == False and len(input) != 0:
    list = df.loc[df['Name'].str.contains(input, case = False)]
    list.sort()
    option = st.selectbox('Select Game', list)
    #filter = st.selectbox("Filter by Platform", (df.loc[df['Platform'] == filter]))
    #df = df.loc[df['Platform'] == filter]
    curr = df.loc[df['Name'] == option]
    st.table(curr)

table = st.radio('Display Table', ["yes", "no"])
if table == 'yes':
    st.dataframe(sf, 100000, 500)
