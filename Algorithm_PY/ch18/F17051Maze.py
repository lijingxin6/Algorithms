# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 10:50 AM 5/19/20

Question: 

"""
from AdjListGraph import Graph
from AdjListGraph import Vertex

def dfs(matrix, start, dest):
    visited = [[False] * len(matrix[0]) for i in range(len(matrix))]  # 二维数组  作为 set
    return dfsHelper(matrix, start, dest, visited)


def dfsHelper(matrix, start, dest, visited):  # start和dest 传的都是tuple  (x, y)
    if matrix[start[0]][start[1]] == 1:  # 开始点 是个墙  不能走
        return False

    if visited[start[0]][start[1]]:  # 已经被访问过了, 就不需要继续走了
        return False
    if start[0] == dest[0] and start[1] == dest[1]:  # 开始点和终止点的(x,y)相同 => 找到了 => True
        return True

    visited[start[0]][start[1]] = True  # start[0] 表示行   start[1]表示列

    # 在 4 个 if 里进行递归
    if (start[1] < len(matrix[0]) - 1):
        r = (start[0], start[1] + 1)
        if (dfsHelper(matrix, r, dest, visited)):
            return True

    if (start[1] > 0):
        l = (start[0], start[1] - 1)
        if (dfsHelper(matrix, l, dest, visited)):
            return True

    if (start[0] > 0):
        u = (start[0] - 1, start[1])
        if (dfsHelper(matrix, u, dest, visited)):
            return True

    if (start[0] < len(matrix[0]) - 1):
        d = (start[0] + 1, start[1])
        if (dfsHelper(matrix, d, dest, visited)):
            return True

    return False
matrix = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
dest  = (4, 4)
dfs(matrix, start, dest)