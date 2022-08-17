import streamlit as st
import pandas as pd

st.title("Queen Problem")
board = [4,5,6,7,8,9,10]
queens = [1,2,3,4,5,6,7,8,9,10]
size = st.select_slider('Board Size', options = board)
input = st.select_slider('Number of Queens', options = queens)


