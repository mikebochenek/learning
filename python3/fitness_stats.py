#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:58:29 2024
pip install calmap <- https://pythonhosted.org/calmap/
pip install july   <- https://stackoverflow.com/questions/32485907/matplotlib-and-numpy-create-a-calendar-heatmap
@author: mike
"""

import pandas as pd
import calmap

filename = '../data_csv/fitness_latest.csv'
df = pd.read_csv(filename)

# example #1 
import numpy as np; np.random.seed(sum(map(ord, 'calmap')))
all_days = pd.date_range('1/15/2014', periods=700, freq='D')
days = np.random.choice(all_days, 500)
events = pd.Series(np.random.randn(len(days)), index=days)
#calmap.yearplot(events, year=2015)

# example #2
import july
from july.utils import date_range
dates = date_range("2024-01-01", "2024-12-31")
data = np.random.randint(0, 1, len(dates))

# events = pd.to_datetime(df.head(8).get('date'),format="%d.%m.%Y")
from datetime import datetime
types = ['','biking', 'swimming','running','football', 'basketball']
start = datetime.strptime('01.01.2024', "%d.%m.%Y")
for d in df.iterrows(): # it ain't pretty, but does the job 
    date = d[1][2]
    if (isinstance(date, str) and ('2024' in date)):
        dObj = datetime.strptime(date, "%d.%m.%Y")
        diff = dObj - start 
        idx = types.index(d[1][4])
        data[diff.days] = idx
        #print('date', dObj, type(date), d[1][4], diff.days, idx)

july.heatmap(dates, data, title='Fitness Activity', cmap="github")
