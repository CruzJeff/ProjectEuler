# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 01:18:23 2017

@author: User
"""
# I don't know why this works but the formula to get the sum of the square of
# n natural numbers is the gaussian sum multiplied by
# 7, plus 2/3rd for every number above 10 that is part of the sum

def gauss(n):
    result = (n*(n + 1))/2
    return result

def squareGauss(n):
    mult = n - 10
    result = (gauss(n)) * (7.0 + (2/3)*mult)
    return result

answer = (gauss(100)**2) - squareGauss(100)
print(answer)





