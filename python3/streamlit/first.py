'''
https://www.datacamp.com/tutorial/streamlit
https://medium.com/data-and-beyond/streamlit-d357935b9c
[ Sun Oct 29 09:05:19 ~/Documents/learning/streamlit ] streamlit run first.py 
'''

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("My First Line Plot with Streamlit")
data = pd.DataFrame({
    "year": [2001, 2004, 2005, 2007, 2008, 2015],         
    "salary": [85000, 52000, 80000, 105000, 130000, 139000]})
plt.plot(data["year"], data["salary"]) # Plot the data
st.pyplot()  # Show the plot in the Streamlit app
st.dataframe(data)

st.title ("It's fun and addictive")
st.header("because it looks pretty")
st.markdown("..and because it's fast")
st.code("pip3 install streamlit")
st.subheader("can also quickly generate latex (math)")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')


st.markdown("___")
st.header("more cut and paste examples")
st.write("from https://docs.streamlit.io/library/get-started/main-concepts")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.write("super easy to also plot a map based on GPS coords")
#map_data = pd.DataFrame(
#    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
#st.map(map_data)
