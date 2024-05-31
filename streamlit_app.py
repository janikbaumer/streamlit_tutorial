# tutorial day 2

import streamlit as st

st.write('Hello World!')

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')



# Import pandas library
import pandas as pd
# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]] 
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])
# print dataframe.
st.write(df)

df
