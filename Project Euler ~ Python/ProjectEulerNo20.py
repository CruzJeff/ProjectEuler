<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 10:45:44 2017

@author: User
"""

'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

import math

fact_100 = str(math.factorial(100))
result = 0

for digit in fact_100:
    result += int(digit)

=======
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 10:45:44 2017

@author: User
"""

'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

import math

fact_100 = str(math.factorial(100))
result = 0

for digit in fact_100:
    result += int(digit)

>>>>>>> origin/master
print(result)