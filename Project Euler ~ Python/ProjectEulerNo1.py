# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:19:56 2017

@author: Zeox
"""
result = 0

for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
        result += x
print(result)
