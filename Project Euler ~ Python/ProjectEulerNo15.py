# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 01:15:08 2017

@author: User
"""

'''For number 15, for the 2 x 2 grid we have to go down 2 times, and
right 2 times to get to the opposite corner. From this we can see that
for an N by N grid, you would have to go down N times, and to the
right N times. So for a 20x20 grid, the question is from 40 moves,
how many different ways can we choose to go down/right 20 times.'''


'''In statistics this is a combination, 40 choose 20 (Because if we
choose 20 positions for Down/Right, the empty spots automatically
become the other direction) '''


import math

def ncr(n,k):
    numerator = math.factorial(n)
    denominator = math.factorial(k) * math.factorial(n-k)
    return numerator/denominator
    
    
print(ncr(40,20))