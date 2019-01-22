<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 20:23:10 2018

@author: User
"""

"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


import time
start = time.time()
fiblist = [0 for x in range(1000000)] #Using a list for memoization

#Fibonacci Function
def fib(x):
    if x == 0:
        fiblist[x] = 0
        return 0
    elif x == 1:
        fiblist[x] = 1
        return 1
    elif x == 2:
        fiblist[x] = 2
        return 2   
    elif fiblist[x] != 0.0:
        return fiblist[x]
    else:
        fiblist[x] = fib(x-1) + fib(x-2)
        return fiblist[x]

#Loop to get answer
answer = 0
x = 0
while len(str(answer)) != 1000:
    if x > 999999:
        fiblist[x] = 0
    answer = fib(x)
    x += 1
    if x % 100 == 0 :
        print(x)
        
elapsed = (time.time() - start)
print(elapsed)
print("Answer:",x)
    
=======
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 20:23:10 2018

@author: User
"""

"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


import time
start = time.time()
fiblist = [0 for x in range(1000000)] #Using a list for memoization

#Fibonacci Function
def fib(x):
    if x == 0:
        fiblist[x] = 0
        return 0
    elif x == 1:
        fiblist[x] = 1
        return 1
    elif x == 2:
        fiblist[x] = 2
        return 2   
    elif fiblist[x] != 0.0:
        return fiblist[x]
    else:
        fiblist[x] = fib(x-1) + fib(x-2)
        return fiblist[x]

#Loop to get answer
answer = 0
x = 0
while len(str(answer)) != 1000:
    if x > 999999:
        fiblist[x] = 0
    answer = fib(x)
    x += 1
    if x % 100 == 0 :
        print(x)
        
elapsed = (time.time() - start)
print(elapsed)
print("Answer:",x)
    
>>>>>>> origin/master
