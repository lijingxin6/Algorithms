# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 8:23 PM 4/10/20

a = [[0] * 8] * 8
a[0][0] = 9
a

"""

def zero(matrix):
    m = [None] * len(matrix)
    n = [None] * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                m[i] = 1
                n[j] = 1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(m[i] == 1 or n[j] == 1):
                matrix[i][j] = 0




matrix = [  [ 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
            [ 1, 1, 0, 1, 1, 1, 1, 1, 1, 1 ],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]

for x in matrix:
    print(x, sep=" ")

zero(matrix)

print('-' * 30)
for x in matrix:
    print(x, sep=" ")