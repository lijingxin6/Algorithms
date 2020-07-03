# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 1:06 PM 5/19/20

Question: 

"""
from AdjListGraph import Graph
from AdjListGraph import Vertex

def dfsIterative(matrix, start, dest):
    visited = [[False] * len(matrix[0]) for i in range(len(matrix))]
    stack = []
    stack.append(start)
    visited[start[0]][start[1]] = True

    idxs = [[0, 1], [0, -1], [-1, 0], [1, 0]]  # 代表四个方向:  →  ←  ↑  ↓

    while len(stack) != 0:
        curr = stack.pop()  # vertex
        if (curr[0] == dest[0] and curr[1] == dest[1]):
            return True

        for idx in idxs:  # 相当于 四个if
            x = curr[0] + idx[0]
            y = curr[1] + idx[1]

            if (x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0])):  # 判断  不要越界
                continue

            if (matrix[x][y] == 1):  # wall
                continue

            if (visited[x][y] == True):  # 访问过
                continue
            visited[x][y] = True
            stack.append((x, y))

    return False

matrix = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
dest  = (4, 4)
dfsIterative(matrix, start, dest)