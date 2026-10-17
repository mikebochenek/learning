# -*- coding: utf-8 -*-
"""
Spyder Editor - This is another temporary script file for playing around in 2022
"""

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('/home/mike/ownCloud/Documents/backups/linkedin-export/Connections.csv')
#print(df.info())
companies = (df.groupby(['Company']).size().sort_values(ascending=False))
print(companies.head(20))

# df.groupby(['Company']).size().plot(kind='pie', subplots=True)

# https://seaborn.pydata.org/introduction.html
import seaborn as sns
"""
tips = sns.load_dataset("tips")
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)
"""

# https://stackoverflow.com/questions/46793448/plotting-series-using-seaborn
head = companies.head(25)
sns.barplot(head.values, head.index, orient = 'h')
