# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 00:03:30 2017

@author: User
"""

#Note: Cannot solve directly using cython, goes over C int limit
#Look into alternate solving methods for Cython


#Read the matrix from a .txt file while stripping whitespace characters
matrix = [line.rstrip() for line in open('euler_13_matrix.txt')]

result = 0
for num in matrix:
    result = result + int(num)
    
print("The first 10 digits of the sum are", str(result)[:10])