<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 20:04:30 2018

@author: User
"""

"""
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import itertools

nums = ['0','1','2','3','4','5','6','7','8','9']
permutations = list(itertools.permutations(nums))

for x in range(len(permutations)):
    permutations[x] = "".join(perm for perm in permutations[x])

permutations.sort()

print(permutations[999999])
=======
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 20:04:30 2018

@author: User
"""

"""
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import itertools

nums = ['0','1','2','3','4','5','6','7','8','9']
permutations = list(itertools.permutations(nums))

for x in range(len(permutations)):
    permutations[x] = "".join(perm for perm in permutations[x])

permutations.sort()

print(permutations[999999])
>>>>>>> origin/master
    