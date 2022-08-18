import streamlit as st
import pandas as pd

st.title("Video Game Sales Dataset")
st.image("https://www.minecraft.net/content/dam/games/minecraft/marketplace/mediablock-buzzybees.jpg")
df = pd.read_csv("vgsales.csv", index_col = 0)
sf = df

filter = st.text_input("Filter by Platform")
if df['Platform'].isin([input]).empty == False and len(filter) != 0:
    df = df.loc[df['Platform'] == filter]
    df.reset_index(drop = True)

input = st.text_input("Search for Game")
if df['Name'].isin([input]).empty == False and len(input) != 0:
    filter = st.text_input("Filter by Platform")
    if df['Platform'].isin([input]).empty == False and len(filter) != 0:
        df = df.loc[df['Platform'] == filter]
    df.reset_index(drop = True)
    st.write("Currently filtering for ", filter)
    st.table(df.loc[df['Name'].str.contains(input, case = False)])




table = st.radio('Display Table', ["yes", "no"])
if table == 'yes':
    st.dataframe(sf, 100000, 500)
