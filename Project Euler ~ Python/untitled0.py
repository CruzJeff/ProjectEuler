# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 07:37:47 2017

@author: User
"""


%%cython

import time
def fib(int n):
    cdef int i
    cdef double a=0.0, b=1.0
    for i in range(n):
        a, b = a+b, a
    return a

start = time.time()
fib(9999999)
elapsed = (time.time() - start)
print ("time:", elapsed)




%%cython
import time

def pfib(n):
    a,b = 0.0, 1.0
    for i in range(n):
        a, b = a+b, a
    return a


start = time.time()
pfib(9999999)
elapsed = (time.time() - start)
print ("time:", elapsed)


import time

def pfib(n):
    a,b = 0.0, 1.0
    for i in range(n):
        a, b = a+b, a
    return a


start = time.time()
pfib(9999999)
elapsed = (time.time() - start)
print ("time:", elapsed)