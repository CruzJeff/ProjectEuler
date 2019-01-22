# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 00:49:08 2017

@author: User
"""


import math
import time


def gauss(n):
    result = int((n*(n + 1))/2)
    return result


def factors(n):
    divisors = 0
    for x in range(1,math.ceil((math.sqrt(n)))):
        if n % x == 0:
            divisors += 2
    return divisors



X = 0
N = 0

start = time.time()

while(X <= 500):
    N += 1
    X = factors(gauss(N))
    
elapsed = (time.time() - start)
print(gauss(N), "found in", elapsed, "seconds")
    
