# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('/home/mike/ownCloud/Documents/linkedin-export/Connections.csv')
#print(df.info())
companies = (df.groupby(['Company']).size().sort_values(ascending=False))
print(companies.head(20))

# df.groupby(['Company']).size().plot(kind='pie', subplots=True)

