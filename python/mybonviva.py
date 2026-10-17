#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 18:13:16 2024
@author: mike
"""
import pandas as pd
import calmap
import platform

# https://facebook.github.io/prophet/docs/quick_start.html#python-api
from prophet import Prophet
def hello_prophet():
    df = pd.read_csv('https://raw.githubusercontent.com/facebook/prophet/main/examples/example_wp_log_peyton_manning.csv')
    df.head()
    m = Prophet()
    m.fit(df)
    future = m.make_future_dataframe(periods=365)
    future.tail()
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    fig1 = m.plot(forecast)
    
# hello_prophet()

filename = 'c:/Users/user/ownCloud/Documents/bills/bonviva/SC-Transactions_2024-05-26_11-01-45.csv'
if ('Windows' == platform.system()):
    pass # was 'Nil' before to keep default  # https://stackoverflow.com/questions/690622/whats-a-standard-way-to-do-a-no-op-in-python
else:
    filename = '/home/mike/ownCloud/Documents/bills/bonviva/SC-Transactions_2024-05-26_11-01-45.csv'

df = pd.read_csv(filename)
df.info()
print ('\naverage amount:', df['Amount'].mean())


