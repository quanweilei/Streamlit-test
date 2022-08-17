import streamlit as st
import pandas as pd

st.title("Calculator Test App")
option = st.selectbox('Select One', 'Addition', 'Subtraction', 'Multiplication', 'Division')
st.write('You selected', option)