# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 2:41 PM 5/21/20

Question: 

"""

def updateMatrix(matrix):
    q, m, n = [], len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] != 0:
                matrix[i][j] = 0x7fffffff # 非0的地方设置成最大值 因为要找最小值
            else:
                q.append((i, j)) # 把所有的0放进stack
    for i, j in q:
        for r, c in ((i, 1+j), (i, j-1), (i+1, j), (i-1, j)):
            z = matrix[i][j] + 1
            if 0 <= r < m and 0 <= c < n and matrix[r][c] > z: # 找 neighbor
                matrix[r][c] = z
                q.append((r, c))
    return matrix

matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 1, 1],
]
updateMatrix(matrix)