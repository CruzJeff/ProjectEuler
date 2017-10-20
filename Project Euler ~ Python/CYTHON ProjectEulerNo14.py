# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 00:48:37 2017

@author: User
"""
%%cython

import time

cdef unsigned int chain = 1

cdef collatz(unsigned long int n):
    global chain
    if n < 0:
        print("This function is defined for non-negative integers")
        return ValueError
    elif n == 0:
        return 0
    elif n == 1:
        result = chain
        chain = 1
        return result
    elif n%2 == 0:
        chain = chain + 1
        return collatz(int(n/2))
    else:
        chain = chain + 1
        return collatz((3 * n) + 1)
        
        
cdef unsigned int maximum = 0
cdef unsigned int answer = 0
cdef unsigned int current = 0

start = time.time()
cdef unsigned int x
for x in range(1000000):
    current = collatz(x)
    if current > maximum:
        maximum = current
        answer = x

    
elapsed = (time.time() - start)
print("The starting number under 1M that causes the longest chain is ", answer)
print("Found in", elapsed, "seconds")
#Answer Found in 1.16 compared to Pure Python's 57 seconds