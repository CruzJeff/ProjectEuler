# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 13:40:32 2017

@author: User
"""

%%cython
import math
import time
start = time.time()

cdef f(unsigned int k, n):
    if n == 0:
        return 1
    result = 0
    for i in range(n+1):
        result += f(k,math.floor(i/k))
    return result

print(f(2,10))

elapsed = (time.time() - start)
print("Found in", elapsed, "seconds")



def f(k,n):
    t = 0  
    high = k
    result = 0
    step = 1
    Flags = []
    
    #For Loop to get the points for which the steps increase
    while t < n:
        t += k ** 2
        Flags.append(t)
    
    Index = 0
    
    #Main Loop
    for x in range(0,n+1):
        #Special Case for K = 2, there seems to be a different behavior in steps
        if k == 2:
            if x < high:
                result += step
            else:
                if high < 4:
                    step = high
                    high += k
                    result += step
                else:
                    step = high
                    high += k
                    result += step
            
        else:
            if Flags != []:
                if x == Flags[Index]:
                    Index += 1
            
            if x < high:
                result += step
            
            else:
                high += k
                step += Index + 1
                result += step
            
    return result

fd= 0
for x in range(3,11):
    fd += f(x,int(10e14))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            