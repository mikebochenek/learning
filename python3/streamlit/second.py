'''
Sun Jan  7 14:35:58 CET 2024
https://docs.streamlit.io/library/advanced-features/widget-behavior
'''

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def affordability(income, price, down):
    equity = down / price
    amortization = 0 # TODO
    mortgage = price - down
    monthly_cost = (mortgage * 0.06 + amortization) / 12
    monthly_income = income/12*0.33 # how much can be afforded monthly
    print ('  own equity', equity, 'monthly', monthly_cost, 'vs.', monthly_income)
    return (equity >= 0.2) and (monthly_cost <= monthly_income)

def recalc():
    a = affordability(income, price, down)

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Mortgage calculator")

income = st.slider('yearly income', 0, 1000000, value=100000, step=1000, on_change=recalc)
down = st.slider('down payment', 0, 10000000, value=200000, step=1000, on_change=recalc)
price = st.slider('purchase price', 0, 10000000, value=1000000, step=1000, on_change=recalc)
