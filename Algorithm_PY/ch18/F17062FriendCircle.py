# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 5:11 PM 5/20/20

Question: 

"""

def findCircleNum(M):
    circle = 0
    n = len(M)
    for i in range(n): # 对每个人来运行dfs
        if M[i][i] != 1:
            continue
        friends = [i] # 相当于是stack,运行完就找到第i个人的所有朋友
        while friends:
            f = friends.pop()
            if M[f][f] == 0:
                continue
            M[f][f] = 0 # 自己不认识自己,说明已经访问过了
            for j in range(n):
                if M[f][j] == 1 and M[j][j] == 1:
                    friends.append(j)
        circle += 1
    return circle


def findCircleNum2(M):
    def dfs(node):
        visited.add(node)
        for friend in range(len(M)):
            if M[node][friend] and friend not in visited:
                dfs(friend)

    circle = 0
    visited = set()
    for node in range(len(M)):
        if node not in visited:
            dfs(node)
            circle += 1
    return circle

M = [
     [1,1,0],
     [1,1,0],
     [0,0,1]]
findCircleNum2(M)
