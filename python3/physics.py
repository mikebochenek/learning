#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
motivated by study with Luke & https://github.com/rougier/scientific-visualization-book
"""

def velocity(t, t0, s, s0):
    return (s-s0) / (t-t0)

def convert_to_km_per_h(v):
    return 0

result = velocity(41.8,32,100,0)
print(f"{result:.2f}", 'm/s')

def strecke_at(t, t0, s0, v):
    return v * (t-t0) + s0

print(strecke_at(6, 1, 0, 10))