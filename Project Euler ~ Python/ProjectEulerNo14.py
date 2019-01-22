<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 00:17:54 2017

@author: User
"""
import time

chain = 1

def collatz(n):
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
        return collatz(n/2)
    else:
        chain = chain + 1
        return collatz((3 * n) + 1)
        
        
maximum = 0
answer = 0
current = 0

start = time.time()

for x in range(1000000):
    current = collatz(x)
    if current > maximum:
        maximum = current
        answer = x

    
elapsed = (time.time() - start)
print("The starting number under 1M that causes the longest chain is ", answer)
=======
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 00:17:54 2017

@author: User
"""
import time

chain = 1

def collatz(n):
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
        return collatz(n/2)
    else:
        chain = chain + 1
        return collatz((3 * n) + 1)
        
        
maximum = 0
answer = 0
current = 0

start = time.time()

for x in range(1000000):
    current = collatz(x)
    if current > maximum:
        maximum = current
        answer = x

    
elapsed = (time.time() - start)
print("The starting number under 1M that causes the longest chain is ", answer)
>>>>>>> origin/master
print("Found in", elapsed, "seconds")