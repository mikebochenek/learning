# -*- coding: utf-8 -*-
"""
Spyder Editor: This is a temporary script file.  - hope that it doesn't get deleted..?
https://github.com/mikebochenek/python-notebooks/blob/master/YakondiStats.ipynb
"""

import matplotlib.pyplot as plt
import pandas as pd
import pymysql.cursors
import json

def fetchData(sql):
    connection = pymysql.connect(host='localhost', user='test2', password='test2', db='beta', cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
    finally:
        connection.close()
    return rows

users = pd.DataFrame(fetchData("select count(*) as c, role from Users group by role"))

country_tags = pd.DataFrame(fetchData("""select count(*) as total, t.tag_name as country from Tags t 
    join TagReferences tr on tr.tag_id = t.tag_id and t.status = 3
    join Users u on u.user_id = tr.ref_id and u.role = 'ADVISER'
    group by t.tag_name order by total desc""" ))

df = pd.DataFrame(fetchData("""select user_id,currentLocation,misc from Users where role = 'adviser' 
  order by user_id desc"""))  # convert rows from fetch into data frame
df = df.dropna(axis=0, how='any')
l = []
for index, row in df.iterrows():
    j = json.loads(row['misc'])
    l.append(j['countryCode'])

from collections import Counter

x = Counter(l)    
countries = sorted(x.items(), key=lambda i: i[1], reverse=True)

#plt.pie(users.c, labels=users.role, autopct='%1.1f%%')
#plt.pie(country_tags.total.head(20), labels=country_tags.country.head(20), autopct='%1.1f%%')
plt.barh(country_tags.country.head(25), width=country_tags.total.head(25), color="green")
