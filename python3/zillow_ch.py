#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:42:27 2023
"""

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('/home/mike/Downloads/swiss-zillow/Distribution_of_income.csv') #'Distribution_of_income.csv')
# print(df.info())

def calcP(d):
    sumt = d['NUMBER_OF_TAXPAYERS'].sum()
    d = d.sort_values(by=['INCOME_GROUP_CODE'], ascending=False)
    d['percentage'] = d['NUMBER_OF_TAXPAYERS'] / sumt * 100
    return d[['INCOME_GROUP_CODE', 'percentage']]

zollikon = calcP(df.query('MUNICIPALITY == "Zollikon" & YEAR == 2011'))
maur = calcP(df.query('MUNICIPALITY == "Maur" & YEAR == 2011'))
