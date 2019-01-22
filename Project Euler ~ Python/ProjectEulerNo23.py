<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 19:46:54 2018

@author: User
"""
'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
import time


#Function to get sum of divisors
def d(n):
    divisors = []
    for x in range(1,n):
        if n % x == 0:
            divisors.append(x)
    return sum(divisors)

#Lists to hold abundant numbers and copy of it
abundant = []
abundant2 = []  #Could be optimized to not require this copy
start = time.time()

#Loop to get list of abundant numbers
for i in range(12,28123):
    if d(i) > i:
        abundant.append(i)
        abundant2.append(i)
        
        
print("Step 1 done")
#The greatest number that cannot be expressed as an abundant sum is less than 28123
#List to hold all sums of abundant numbers
sums = []

#Loop to calculate all sums of abundant numbers less than 28123
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
for z in range(20162):
    print(z)
    for k in range(last_index,len(sums)):
        if z == sums[k]:
            last_index = k
            break
        elif sums[k] > z:
            answer += z
            last_index = k
            break    
elapsed = (time.time() - start)
print(elapsed)
print(answer)

=======
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 19:46:54 2018

@author: User
"""
'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
import time


#Function to get sum of divisors
def d(n):
    divisors = []
    for x in range(1,n):
        if n % x == 0:
            divisors.append(x)
    return sum(divisors)

#Lists to hold abundant numbers and copy of it
abundant = []
abundant2 = []  #Could be optimized to not require this copy
start = time.time()

#Loop to get list of abundant numbers
for i in range(12,28123):
    if d(i) > i:
        abundant.append(i)
        abundant2.append(i)
        
        
print("Step 1 done")
#The greatest number that cannot be expressed as an abundant sum is less than 28123
#List to hold all sums of abundant numbers
sums = []

#Loop to calculate all sums of abundant numbers less than 28123
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
for z in range(20162):
    print(z)
    for k in range(last_index,len(sums)):
        if z == sums[k]:
            last_index = k
            break
        elif sums[k] > z:
            answer += z
            last_index = k
            break    
elapsed = (time.time() - start)
print(elapsed)
print(answer)

>>>>>>> origin/master
