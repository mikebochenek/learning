#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 09:56:13 2022 - motived by https://codefol.io/posts/the-forty-year-programmer/
@author: mike
- a bit weird that auto-complete does not work as expected
- nice new shortcut: control-enter (re)run current line (like SQL Developer)
"""
import pandas as pd
from datetime import datetime

startTime = datetime.now()

df = pd.read_csv("/home/mike/Documents/aoc/day7-0.txt") # print(df.info)

df = pd.read_csv('/home/mike/ownCloud/Documents/backups/linkedin-export/Connections.csv')
companies = (df.groupby(['Company']).size().sort_values(ascending=False))
# print(df.tail(20))     # last 20
# print(df.iloc[::2, 0]) # even/odd
print(df.iat[24,4])      # https://note.nkmk.me/en/python-pandas-at-iat-loc-iloc/

df = pd.read_csv("/home/mike/Documents/opendata/ds_salaries.csv") 
print(df["salary_in_usd"].mean())
#print(df.describe())
#print(df.groupby(["employee_residence"]).size())
#print(df.groupby(["employee_residence"]).mean())

print(datetime.now() - startTime, 'linkedin-export shape:', df.shape) 
