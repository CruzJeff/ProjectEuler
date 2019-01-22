# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 10:17:39 2018

@author: User
"""


'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

#Dictionary of letter values
alphabet = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,
            'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,
            'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

#Function to get name_score
def name_score(name):
    result = 0
    for letter in name:
        result += alphabet[letter]
    return result
    
#Reading the file and putting names into list
file = "names.txt"
names = []
for line in open(file,'r'):
    names.append(line.strip().split(','))

names = names[0]
names.sort()


#Getting Answer
answer = 0
for x in range(len(names)):
    names[x] = names[x].replace('"',"") #Remove the " from names
    answer += name_score(names[x]) * (x+1)

print(answer)