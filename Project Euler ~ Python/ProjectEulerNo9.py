# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 02:56:50 2017

@author: User
"""


def euclid(m, n):
    a = m**2 - n**2
    b = 2 * m * n
    c = m**2 + n**2
    return a,b,c

for x in range(1000):
    for y in range(1000):
        a,b,c = euclid(x,y)
        if a > 0 and a + b + c == 1000:
            answer = a * b * c
            A = a
            B = b
            C = c

print("The answer is", A, "times", B ,"times", C, "which is", answer)
            
        
    