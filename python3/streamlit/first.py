'''
https://www.datacamp.com/tutorial/streamlit
https://medium.com/data-and-beyond/streamlit-d357935b9c
[ Sun Oct 29 09:05:19 ~/Documents/learning/streamlit ] streamlit run first.py 
'''

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dateutil import parser
from datetime import datetime

st.title("My First Line Plot with Streamlit")
data = pd.DataFrame({
    "year": [2001, 2004, 2005, 2007, 2008, 2015],         
    "salary": [85000, 52000, 80000, 105000, 130000, 139000]})
plt.plot(data["year"], data["salary"]) # Plot the data
st.pyplot()  # Show the plot in the Streamlit app
# st.dataframe(data)

officepresence = pd.DataFrame({
    "month": ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october"],
    "percentage": [50, 70, 52, 50, 53, 64, 46, 53, 52, 57]
})
st.dataframe(officepresence)

st.title ("It's fun and addictive")

birth = parser.parse('1979-03-11')
ch = parser.parse('2011-05-28')
today = datetime.today() #.date()  # datetime.date(datetime.now())
age = today - birth

# st.write(age)
# st.write((today-ch) / age)

countries = pd.DataFrame({
    "country": ['pl', 'de', 'ca', 'us', 'ch'],         
    "days": [3800, 630, 4000, 2000, (today-ch).days]})

fig, ax = plt.subplots()
ax.pie(countries.days, labels=countries.country)
st.pyplot()

st.header("because it looks pretty")
st.markdown("..and because it's fast and easy to install:")
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
