# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:27:30 2017

@author: User
"""

import numpy as np
fiblist= np.zeros(100)

def fib(x):
    if x == 0:
        fiblist[x] = 0
        return 0
    if x == 1:
        fiblist[x] = 1
        return 1
    if x == 2:
        fiblist[x] = 2
        return 2   
    if fiblist[x] != 0.0:
        return fiblist[x]
    else:
        fiblist[x] = fib(x-1) + fib(x-2)
        return fiblist[x]

result = 0
i = 0

while (fib(i)<4000000):
    if fib(i) % 2 == 0:
        result += fib(i)
    i+=1
print(result)
    