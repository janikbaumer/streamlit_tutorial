import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from vega_datasets import data
from matplotlib import pyplot as plt

st.header('Display text')
st.header('st.write')
st.write('Hello, *World!* :sunglasses:')
# h = 'Hello, World! smiley'
# h

st.header('Displax numbers')
st.write(1234)

st.header('Display DataFrame')
data_rows = [[1, 10], [2, 20], [3, 30], [4, 40]]
# alternative:
data_dict = {
    'first column' : [1, 2, 3, 4],
    'second column' : [10, 20, 30, 40]
}

df = pd.DataFrame(data=data_rows, columns=['first column', ' second column']) # , index=['r1', 'r2', 'r3', 'r4'])
st.write(df)

st.header('Accept multiple arguments')
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

st.header('Display charts')
# load a simple dataset as a pandas DataFrame
# cars = data.cars()
#plt = alt.Chart(cars).mark_point().encode(
#    x='Horsepower',
#    y='Miles_per_Gallon',
#    color='Origin',
#)

x = np.random.rand(50)
y = np.random.rand(50)
size = np.random.rand(50)
size *= 20
fig, ax = plt.subplots()
scatter = ax.scatter(x, y, s=size)
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_title('scatter plot with random values')
st.pyplot(fig)

