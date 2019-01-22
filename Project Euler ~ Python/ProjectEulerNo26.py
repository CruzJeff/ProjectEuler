<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 20:44:43 2018

@author: User
"""
import math

def sieve_of_eratosthenes(lim):
    if lim < 0:
        print("Error")
    Primes = []
    A = [0 for x in range(lim)]
    A[0] = 1
    A[1] = 1
    MAX = math.floor(math.sqrt(lim))
    for i in range(2,MAX+1):
        if A[i] == 0.0:
            for j in range(i*i,lim,i):
                A[j] = 1
    for x in range(len(A)):
        if A[x] == 0:
            Primes.append(x)
    return Primes

    

primes_under_1000 = sieve_of_eratosthenes(1000)
primes_under_1000.sort(reverse=True)

#Prime number denominators cause long repeated cycles in decimal form
#Guessed first couple off this list and turns out the answer was 983
=======
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 20:44:43 2018

@author: User
"""
import math

def sieve_of_eratosthenes(lim):
    if lim < 0:
        print("Error")
    Primes = []
    A = [0 for x in range(lim)]
    A[0] = 1
    A[1] = 1
    MAX = math.floor(math.sqrt(lim))
    for i in range(2,MAX+1):
        if A[i] == 0.0:
            for j in range(i*i,lim,i):
                A[j] = 1
    for x in range(len(A)):
        if A[x] == 0:
            Primes.append(x)
    return Primes

    

primes_under_1000 = sieve_of_eratosthenes(1000)
primes_under_1000.sort(reverse=True)

#Prime number denominators cause long repeated cycles in decimal form
#Guessed first couple off this list and turns out the answer was 983
>>>>>>> origin/master
