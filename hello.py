import streamlit as st
import pandas as pd

st.write("# Hello World")

x = 12.34567
st.write(x)

df = pd.DataFrame({
    'first_column':[1,2,3,4],
    'second_column': [10,20,30,40]
})

st.write(df)
st.write("# Magic command")
x = 10
x
