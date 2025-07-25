# introduction to streamlit framework : streamlit in an open_source app framework for machine learning and data science projects. it allows you to create web applications for your machine learning and data science projects with simple python scripts. ( a faster way build and share data apps for ml )

# import
# import streamlit
import streamlit as st
import pandas as pd
import numpy as np


# Title of the aplication
st.title('Hello streamlit')


# Display a simple text
st.write('This is a simple text...')


# create a simple dataframe
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})