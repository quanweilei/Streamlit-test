import streamlit as st
import pandas as pd

st.title("Queen Problem")
size = st.select_slider('Board Size', options = [1, 10])
input = st.select_slider('Number of Queens', options = [1, 10])


