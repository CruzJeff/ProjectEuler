<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 23:47:30 2017

@author: User
"""
import math
import numpy as np

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

number = 600851475143 

n = math.ceil(math.sqrt(number))

Primes = sieve(n)

result = 0

for x in range(2,n):
    if number % x == 0 and Primes[x] == 0 and x > result:
        result = x

print(result)
                
            
=======
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 23:47:30 2017

@author: User
"""
import math
import numpy as np

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

number = 600851475143 

n = math.ceil(math.sqrt(number))

Primes = sieve(n)

result = 0

for x in range(2,n):
    if number % x == 0 and Primes[x] == 0 and x > result:
        result = x

print(result)
                
            
>>>>>>> origin/master
        