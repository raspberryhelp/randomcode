import streamlit as st
import pandas as pd
import numpy as np


st.title("Welcome to titles.")
st.text("Welcome to text.")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.text("There's really nothing here so far, but I intend to add some stuff")
st.text("In the meantime, have random facts and charts I guess")

input = st.text_input("Enter something random", "")
st.write({input})