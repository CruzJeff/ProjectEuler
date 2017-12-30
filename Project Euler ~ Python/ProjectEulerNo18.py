# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 17:14:48 2017

@author: User
"""

#Copy paste the raw tree 
tree_string = '''75    
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''


cur = ''
tree = []
index = []

#For loop to create tree as an int array 
for num in tree_string:
    if num != '\n' and num != ' ':
        cur = cur + num
    if len(cur) == 2:
        if cur[0] == '0':
            tree.append(int(cur[1]))
        else:
            tree.append(int(cur))
        cur = ''
        
#List that contains the indices of each row
index_tree = [[0],
 [1, 2],
 [3, 4, 5],
 [6, 7, 8, 9],
 [10, 11, 12, 13, 14],
 [15, 16, 17, 18, 19, 20],
 [21, 22, 23, 24, 25, 26, 27],
 [28, 29, 30, 31, 32, 33, 34, 35],
 [36, 37, 38, 39, 40, 41, 42, 43, 44],
 [45, 46, 47, 48, 49, 50, 51, 52, 53, 54],
 [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65],
 [66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77],
 [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
 [91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104],
 [105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]]


#Solver Function
#Solves the problem by going bottom up from the 2nd to last row, and choosing the best choice from there
#The best choice for each element in the 2nd to last row is added to that element
#and the last row is then removed
#This is repeated until only the root node is left, which will contain the answer

def dynamic_solver(tree):
    level = 13
    for row in range(2,16):
        current_row = index_tree[-row]
        last_row = index_tree[-row + 1]
        for x in current_row:
            tree[x] = max(tree[x] + tree[x+1+level], tree[x] + tree[x+2+level])
        tree = [v for i,v in enumerate(tree) if i not in last_row]
        level = level-1
    return tree

print(dynamic_solver(tree))
