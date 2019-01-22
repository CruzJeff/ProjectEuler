<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 03:04:43 2017

@author: User
"""

left = 0
right = 0
answer = 0
MAX = 0


for i in range(100,1000):
    for j in range(100,1000):
        answer = i * j
        string = str(answer)
        if string == string[::-1] and answer > MAX:
            MAX = answer
            left = i
            right = j
        
print("The answer is",left,"times", right ,"which is", MAX)
=======
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 03:04:43 2017

@author: User
"""

left = 0
right = 0
answer = 0
MAX = 0


for i in range(100,1000):
    for j in range(100,1000):
        answer = i * j
        string = str(answer)
        if string == string[::-1] and answer > MAX:
            MAX = answer
            left = i
            right = j
        
print("The answer is",left,"times", right ,"which is", MAX)
>>>>>>> origin/master
    