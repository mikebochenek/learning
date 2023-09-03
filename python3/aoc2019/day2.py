#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 15:34:36 2023
@author: mike
"""

def runp(p):
    for i in range(0, len(p)):
        if (i % 4 == 0):
            if (p[i] == '1'):
                p[int(p[i+3])] = int(p[int(p[i+1])]) + int(p[int(p[i+2])])
            elif (p[i] == '2'):
                p[int(p[i+3])] = int(p[int(p[i+1])]) * int(p[int(p[i+2])])
            elif (p[i] == '99'):
                #print(p[0])
                return(p[0])

assert(3500==runp('1,9,10,3,2,3,11,0,99,30,40,50'.split(',')))

with open('/home/mike/Documents/aoc/2019/day_2.txt') as f:
    lines = f.read().splitlines()

p = lines[0].split(',')
p[1]='12'
p[2]='2'
runp(p)
