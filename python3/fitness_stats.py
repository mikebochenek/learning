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

filename = '/home/mike/ownCloud/fitness_March8_2024.csv'
df = pd.read_csv(filename)

# example #1 
import numpy as np; np.random.seed(sum(map(ord, 'calmap')))
all_days = pd.date_range('1/15/2014', periods=700, freq='D')
days = np.random.choice(all_days, 500)
events = pd.Series(np.random.randn(len(days)), index=days)
# calmap.yearplot(events, year=2015)

# example #2
import july
from july.utils import date_range
dates = date_range("2024-01-01", "2024-08-31")
data = np.random.randint(0, 14, len(dates))
# july.heatmap(dates, data, title='Fitness Activity', cmap="github")

events = pd.to_datetime(df.head(8).get('date'),format="%d.%m.%Y")

