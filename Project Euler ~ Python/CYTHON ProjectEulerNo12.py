<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 00:49:08 2017

@author: User
"""


%%cython
import math
import time


cdef gauss(unsigned long int n):
    cdef unsigned int result = (int)((n*(n + 1))/2)
    return result


cdef factors(unsigned long int n):
    cdef unsigned int divisors = 0
    cdef unsigned int x = 1
    for x in range(1,math.ceil((math.sqrt(n)))):
        if n % x == 0:
            divisors += 2
    return divisors



cdef unsigned int X = 0
cdef unsigned int N = 0

start = time.time()

while(X <= 500):
    N+=1
    X = factors(gauss(N))
    
elapsed = (time.time() - start)
print(gauss(N), "found in", elapsed, "seconds")

=======
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 00:49:08 2017

@author: User
"""


%%cython
import math
import time


cdef gauss(unsigned long int n):
    cdef unsigned int result = (int)((n*(n + 1))/2)
    return result


cdef factors(unsigned long int n):
    cdef unsigned int divisors = 0
    cdef unsigned int x = 1
    for x in range(1,math.ceil((math.sqrt(n)))):
        if n % x == 0:
            divisors += 2
    return divisors



cdef unsigned int X = 0
cdef unsigned int N = 0

start = time.time()

while(X <= 500):
    N+=1
    X = factors(gauss(N))
    
elapsed = (time.time() - start)
print(gauss(N), "found in", elapsed, "seconds")

>>>>>>> origin/master
