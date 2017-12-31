# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 10:59:50 2017

@author: User
"""

'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000
'''

#Function to get sum of proper divisors
def d(n):
    divisors = []
    for x in range(1,n):
        if n % x == 0:
            divisors.append(x)
    return sum(divisors)


#List to hold all the amicable numbers
amicables = []

#For loop to find all the amicable numbers
for x in range(1,10000):
    y = d(d(x))  
    if y == x and x != d(x):  #Check for perfect numbers and duplicates
        if x not in amicables:
            amicables.append(x)
        if y not in amicables:
            amicables.append(y)

print(amicables)
print(sum(amicables))
        