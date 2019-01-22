# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 03:49:13 2017

@author: User
"""

import numpy as np
import math

def sieve(lim):
    
    A = np.zeros(lim)
    A[0] = 1
    A[1] = 1
    MAX = math.floor(math.sqrt(lim))
    for i in range(2,MAX+1):
        if A[i] == 0.0:
            for j in range(i*i,lim,i):
                A[j] = 1
    return A


primes = sieve(2000000)
result = 0

for x in range(2000000):
    if primes[x] == 0:
        result += x

print(result)