# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 01:55:28 2017

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


primes = sieve(5000000)

counter = 0
i = 0


while(counter<10001):
    if primes[i] == 0:
        counter += 1
    i+=1

print(i-1)
print(counter)
    