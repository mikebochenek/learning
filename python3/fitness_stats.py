#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:58:29 2024
@author: mike
"""

import pandas as pd

filename = '/home/mike/ownCloud/fitness_March8_2024.csv'
df = pd.read_csv(filename)

print (df.head)