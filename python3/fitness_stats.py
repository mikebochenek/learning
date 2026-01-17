#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:58:29 2024
pip install calmap <- https://pythonhosted.org/calmap/
pip install july   <- https://stackoverflow.com/questions/32485907/matplotlib-and-numpy-create-a-calendar-heatmap
@author: mike
"""

import pandas as pd
import platform
from datetime import datetime

startTime = datetime.now()
filename = 'C:\\Users\\User\\ownCloud\\Documents\\fitness\\fitness_2026_01_17.csv'
# filename = '/home/mike/Documents/code/learning/data_csv/fitness_latest.csv'
outfilename = 'C:\\Users\\User\\ownCloud\\Documents\\fitness\\fitness_latest.png'
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
dates = date_range("2026-01-01", "2026-12-31")
data = np.random.randint(0, 1, len(dates))

# events = pd.to_datetime(df.head(8).get('date'),format="%d.%m.%Y")
from datetime import datetime
types = ['','biking', 'swimming','running','football', 'basketball']
start = datetime.strptime('01.01.2026', "%d.%m.%Y")

count2024=0
count2025=0
count2026=0

for d in df.iterrows(): # it ain't pretty, but does the job 
    date = d[1].iloc[2]  # d[1][2]
    if (isinstance(date, str) and ('2024' in date)):
        count2024 += 1

    if (isinstance(date, str) and ('2025' in date)):
        count2025 += 1

    if (isinstance(date, str) and ('2026' in date)):
        count2026 += 1
        dObj = datetime.strptime(date, "%d.%m.%Y")
        diff = dObj - start 
        idx = types.index(d[1][4]) if d[1][4] in types else 1 # default empty to easy (biking) https://claude.ai/chat/dc7f2b9d-4631-43d7-91cf-36dde1c455f7
        data[diff.days] = idx
        #print('date', dObj, type(date), d[1][4], diff.days, idx)

july.heatmap(dates, data, title='Fitness Activity', cmap="github") #cmap="golden")

# plt.savefig(outfilename)

print ('\t', datetime.now(), '2026:', count2026, '2025:', count2025, '2024:', count2024, 'total fitness entries:', len(df), 
    ' - 2024 avg:', round((count2024*1.0/(52-7)), 2), '2025 avg:', round((count2025*1.0/(52)), 2),
    '2026 avg:', round((count2026*1.0/(52)), 2), #TODO 52 needs manual adjustment!
    '\n\t', int((datetime.now() - startTime).total_seconds() * 1000), 
    'ms expired, on', platform.system(), platform.release(), 'created:', outfilename)
# max 2025 04.09.2025 (week 36) TODO - need to update manually above
# min 2024 1,Thursday,15.02.2024,,running (a.k.a. where it all started - week #7)


# https://stackoverflow.com/questions/3595363/properties-file-in-python-similar-to-java-properties
import configparser
config = configparser.RawConfigParser()
config.read('secrets.txt')
print ('my url', config.get('urls', 'fitness_url'))
