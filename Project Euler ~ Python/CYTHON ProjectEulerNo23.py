# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 19:46:54 2018

@author: User
"""
%%cython
import time

#Running time in Pure Python: 69 seconds
#Running time in Cython: 17 Seconds

#Function to get sum of divisors
cdef d(unsigned long int n):
    divisors = []
    cdef unsigned long int x
    for x in range(1,n):
        if n % x == 0:
            divisors.append(x)
    return sum(divisors)

#Lists to hold abundant numbers and copy of it
abundant = []
abundant2 = []  #Could be optimized to not require this copy
start = time.time()

#Loop to get list of abundant numbers
cdef unsigned long int i
for i in range(12,28123):
    if d(i) > i:
        abundant.append(i)
        abundant2.append(i)
        
        
print("Step 1 done")
#The greatest number that cannot be expressed as an abundant sum is less than 28123
#List to hold all sums of abundant numbers
sums = []

#Loop to calculate all sums of abundant numbers less than 28123
cdef unsigned long int j
cdef unsigned long int k
cdef unsigned long int result
for j in range(len(abundant)):
    for k in range(j,len(abundant2)):
        result = abundant[j] + abundant[k]
        if result > 28123:
            break
        else:
            sums.append(result)
        
sums.sort()
print("Step 2 done")

#Loop to find all numbers less than 28123 that is not in sums
#Optimized to remember the last index that broke the loop in order to run in practical time
last_index = 0
answer = 0

cdef unsigned long int z
cdef unsigned long int a
for z in range(20162):
    print(z)
    for a in range(last_index,len(sums)):
        if z == sums[a]:
            last_index = a
            break
        elif sums[a] > z:
            answer += z
            last_index = a
            break    
elapsed = (time.time() - start)
print(elapsed)
print(answer)

