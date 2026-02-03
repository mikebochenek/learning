#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:42:27 2023
"""

# import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('/home/mike/Downloads/swiss-zillow/Distribution_of_income.csv')
ofinterest = ('Wetzikon', 'Dietikon', 'Egg', 'Maur', 'Rüschlikon', 'Zollikon')

"""
bycode = (df.query('MUNICIPALITY == "Zollikon" & YEAR == 2011 & TAX_RATE_CODE == 2'))
print(bycode['NUMBER_OF_TAXPAYERS'].sum()) # 2687
bycode = (df.query('MUNICIPALITY == "Zollikon" & YEAR == 2011').groupby(['TAX_RATE_CODE']).sum())
print(bycode) # 2687 / 4574
"""

def mid(d): # see ../ruby/zillow-play1.rb
    if d <= 30:
        return d * 10000 - 5000
    elif d <= 45:
        return 300000 + (d - 30) * 50000 - 25000
    else:
        return 0

assert 5000 == mid(1) and 95000 == mid(10)
assert 215000 == mid(22) and 375000 == mid(32) and 925000 == mid(43)

def average(s):
    d = (df.query('MUNICIPALITY == "' + s + '" & YEAR == 2011'))
    totalIncome = 0; totalPayers = 0; runningAverage = 0
    sumt = d['NUMBER_OF_TAXPAYERS'].sum()
    for index, row in d.iterrows():
        midIncome = mid(row['INCOME_GROUP_CODE'])
        count = row['NUMBER_OF_TAXPAYERS']
        totalIncome = totalIncome + midIncome * count
        totalPayers = totalPayers + count
        runningAverage = runningAverage + midIncome * count / sumt
    #print (' DEBUG -> ', runningAverage, 'vs.', (totalIncome / totalPayers))
    return totalIncome / totalPayers

def calcP(d):  #calculate 'percentile' and add to new column
    sumt = d['NUMBER_OF_TAXPAYERS'].sum()
    d = d.sort_values(by=['INCOME_GROUP_CODE'], ascending=False)
    d['percentage'] = d['NUMBER_OF_TAXPAYERS'] / sumt * 100
    return d[['INCOME_GROUP_CODE', 'percentage']]

def score(s): #rough score: higher percentage in higher brackets, gives higher score
    d = calcP(df.query('MUNICIPALITY == "' + s + '" & YEAR == 2011'))
    return ((d['INCOME_GROUP_CODE'] * d['percentage']).sum())

def findpercentile(s, p):
    d = calcP(df.query('MUNICIPALITY == "' + s + '" & YEAR == 2011'))
    d['cumulative'] = d['percentage'].cumsum()
    return d.query('cumulative > ' + str(p)).iloc[0,0]

def findmedian(s):
    return findpercentile(s, 50)

print('\ncity median p90 p95 score average') #of special interest are:
for o in ofinterest:
    print(o, findmedian(o), findpercentile(o, 10), findpercentile(o, 5), "%.1f" % score(o), "%.1f" % average(o))

u = df['MUNICIPALITY'].unique()
for _u in (u):
    s = score(_u)
    m = findmedian(_u)
    p90 = findpercentile(_u, 10)
    if (s > 999): #(s < 540):
        print (' *** ', _u, m, p90, s)
    else:
        None
        #print(_u, m, s)
