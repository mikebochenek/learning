#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 21:45:42 2023
@author: mike
"""

def fuel(mass): # day1-1
    return (int)(mass / 3) - 2

assert(fuel(1969)==654)
assert(fuel(100756)==33583)

def recursive_fuel(mass): #day1-2
    #print (mass, fuel(mass))
    f = fuel(mass)
    if (f <= 0):
        return 0
    else:
        return recursive_fuel(f) + f

assert(recursive_fuel(14) == 2)
assert(recursive_fuel(1969) == 966)
assert(recursive_fuel(100756) == 50346)


with open('c:\\dev\\data\\aoc\\2019_day1.txt') as f:
    lines = f.read().splitlines()

sum = 0
for n in lines:
    sum += recursive_fuel(int(n))
print ('day1',sum)
