# introduction to streamlit framework : streamlit in an open_source app framework for machine learning and data science projects. it allows you to create web applications for your machine learning and data science projects with simple python scripts. ( a faster way build and share data apps for ml )

# import
# import streamlit
import streamlit as st
import pandas as pd
import numpy as np


# # Title of the aplication
# st.title('Hello streamlit')


# # Display a simple text
# st.write('This is a simple text...')


# # create a simple dataframe
# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# })


# # display the dataframe
# st.write('here is the dataframe')
# st.write(df)


# # create a line chart
# chart_data = pd.DataFrame(
#     np.random.randn(20, 3), columns=['a', 'b', 'c']
# )
# st.line_chart(chart_data)


## widgets

# get input from user
name = st.text_input('enter your name: ')

if name:
    st.write(f'hello {name}')


# slider
age = st.slider('select your age: ', 0, 100, 25)
st.write(f'your age is {age}.')


# select box
options = ['python', 'java', 'c++', 'js']
choice = st.selectbox('choose your favorite language:', options)
st.write(f'you selected {choice}.')


# show dataframe
data = {
    'Name': ['ali', 'reza', 'zara', 'amir'],
    'Aga': [20, 30, 40, 50],
    'city': ['a', 'b', 'c', 'd']
}
df = pd.DataFrame(data)
df.to_csv('sampledata.csv')
st.write(df)