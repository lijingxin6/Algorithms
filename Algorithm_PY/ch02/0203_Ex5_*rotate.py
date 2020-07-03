# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 3:33 PM 4/11/20

"""
def rotate(matrix):
    n = len(matrix)
    result = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n-1-i] = result[i][j]
    for x in result:
        print(x, sep=" ")


def rotate_inplace(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            # left --> top
            matrix[first][i] = matrix[last - offset][first]
            # bottom --> left
            matrix[last - offset][first] = matrix[last][last-offset]   # [4][0] <-- [4][4]      [3][0]  <-- [4][3]

            # right --> bottom
            matrix[last][last-offset] = matrix[i][last]
            # top --> right
            matrix[i][last] = matrix[first][i]   # [0][4] <-- [0][0]        [1][4] <-- [0][1]
    for x in matrix:
        print(x, sep=" ")
