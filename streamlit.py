import streamlit as st
import pandas as pd

st.title("Video Game Sales Dataset")
st.image("https://www.minecraft.net/content/dam/games/minecraft/marketplace/mediablock-buzzybees.jpg")
df = pd.read_csv("vgsales.csv", usecols = ['Rank', 'Year', 'Name', 'Genre', 'Publisher', 'Global_Sales'])

df.set_index("Rank", inplace = True)
df.rename(columns = {'Global_Sales': 'Global Sales (Millions)'})

sf = df
df['Year'] = df['Year'].fillna(-1).apply(int)
df.loc[df['Year'] == -1, 'Year'] = 'NA'
df['Year'] = df['Year'].apply(str)

input = st.text_input("Search for Game")
if df['Name'].isin([input]).empty == False and len(input) != 0:
    cf = (df.loc[df['Name'].str.contains(input, case = False)])['Name'].tolist()
    option = st.selectbox('Select Game', set(cf))
    #filter = st.selectbox("Filter by Platform", (df.loc[df['Platform'] == filter]))
    #df = df.loc[df['Platform'] == filter]
    curr = df.loc[df['Name'] == option]
    st.table(curr)


table = st.radio('Display Table', ["yes", "no"])
if table == 'yes':
    st.dataframe(sf, 100000, 1000)
