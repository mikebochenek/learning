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
    a = (equity >= 0.2) and (monthly_cost <= monthly_income)
    st.write(a, 'equity %', equity, 'monthly cost ', monthly_cost, 'vs. income', monthly_income)
    return a

def recalc():
    a = affordability(income, price, down)

htab, mtab, ptab, stab = st.tabs(["home", "mortgage", "properties", "settings"])

with htab:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("buyer/helper/thingy")

with mtab:
    st.header('mortgage + affordability + sbb + tax score')
    income = st.slider('yearly income', 10000, 1000000, value=100000, step=1000, on_change=recalc)
    down = st.slider('down payment', 20000, 10000000, value=200000, step=1000, on_change=recalc)
    price = st.slider('purchase price', 300000, 10000000, value=1000000, step=1000, on_change=recalc)

with ptab:
    st.header("properties")

with stab:
    st.header("settings")

