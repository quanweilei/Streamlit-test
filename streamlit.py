import streamlit as st
import pandas as pd

st.title("Video Game Sales Dataset")
st.image("https://www.minecraft.net/content/dam/games/minecraft/marketplace/mediablock-buzzybees.jpg")
df = pd.read_csv("vgsales.csv", index_col = 0)
table = st.radio('Display Table', ["yes", "no"])
input = st.text_input("Search for Game")
if df['Name'].__contains__(input) == False:
    st.write("Game Does not Exist")
else:
    st.table(df.loc[df['Name'] == input])
if table == 'yes':
    st.dataframe(df, 100000, 500)
