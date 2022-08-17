import streamlit as st
import pandas as pd

while True:
    st.title("Video Game Sales Dataset")
    st.image("https://www.minecraft.net/content/dam/games/minecraft/marketplace/mediablock-buzzybees.jpg")
    df = pd.read_csv("vgsales.csv", index_col = 0)
    table = st.radio('Display Table', ["yes", "no"])
    while table == 'yes':
        st.dataframe(df, 100000, 500)
