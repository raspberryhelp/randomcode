import streamlit as st
import pandas as pd
import numpy as np


st.title("Welcome to titles.")
st.text("Welcome to text.")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
