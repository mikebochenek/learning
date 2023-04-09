#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:42:27 2023
"""

# import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('/home/mike/Downloads/swiss-zillow/Distribution_of_income.csv') #'Distribution_of_income.csv')

"""
print(df.info())
bycode = (df.query('MUNICIPALITY == "Zollikon" & YEAR == 2011 & TAX_RATE_CODE == 2'))
print(bycode['NUMBER_OF_TAXPAYERS'].sum()) # 2687
bycode = (df.query('MUNICIPALITY == "Zollikon" & YEAR == 2011').groupby(['TAX_RATE_CODE']).sum())
print(bycode)
2687 / 4574
"""

def calcP(d):
    sumt = d['NUMBER_OF_TAXPAYERS'].sum()
    d = d.sort_values(by=['INCOME_GROUP_CODE'], ascending=False)
    d['percentage'] = d['NUMBER_OF_TAXPAYERS'] / sumt * 100
    return d[['INCOME_GROUP_CODE', 'percentage']]

zollikon = calcP(df.query('MUNICIPALITY == "Zollikon" & YEAR == 2011'))
maur = calcP(df.query('MUNICIPALITY == "Maur" & YEAR == 2011'))

def score(s):
    d = calcP(df.query('MUNICIPALITY == "' + s + '" & YEAR == 2011'))
    return ((d['INCOME_GROUP_CODE'] * d['percentage']).sum())

def findmedian(s):
    d = calcP(df.query('MUNICIPALITY == "' + s + '" & YEAR == 2011'))
    d['cumulative'] = d['percentage'].cumsum()
    return d.query('cumulative > 50').iloc[0,0]

u = df['MUNICIPALITY'].unique()
for _u in (u):
    s = score(_u)
    m = findmedian(_u)
    if (s > 999): #(s < 540):
        print (' *** ', _u, m, s)
    else:
        None
        #print(_u, m, s)

print('\nRüschlikon', score('Rüschlikon'))
print('Dietikon', findmedian('Dietikon'), score('Dietikon'))
print('Wetzikon', findmedian('Wetzikon'), score('Wetzikon'))
print('Maur', findmedian('Maur'), score('Maur'))
