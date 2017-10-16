# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 03:25:05 2017

@author: User
"""
  
# only has to be really divisible by 11 12 13 14 15 16 17 19 20
# It has to be a multiple of 2520

divisors = [11,12,13,14,15,16,17,18,19,20]
MIN = 9999999999

for x in range(2520,999999999,2520):
    if all(x % y == 0 for y in divisors) and x < MIN:
        MIN = x

print(MIN)
        
        
        
        