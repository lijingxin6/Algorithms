# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 6:19 PM 4/10/20

1. 程序接收三个参数，M，N 和 p，然后生成一个M * N的矩阵，然后每一个cell 有 p 的概率是地雷。
2. 生成矩阵后，再计算出每一个cell周围地雷的数量。

"""

import random

def minesweeper(m,n,p):
    board = [[None] * (n+2) for i in range(m+2)]   # 多 1 行， 多 2 列
    for i in range(1, m+1):
        for j in range(1, n+1):
            r = random.random()
            board[i][j] = -1 if r < p else 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            print("*", end=" ") if board[i][j] == -1 else print(".", end=" ")
        print()

    for i in range(1, m+1):
        for j in range(1, n+1):
            if(board[i][j] != -1):
                for ii in range(i-1, i+2):      ######## 是在第i行的 上边一行 i-1 和 下边一行 i+1
                    for jj in range(j-1, j+2):  ######## 是在第j列的 左边一列 j-1 和 右边一列 j+1
                        if(board[ii][jj] == -1):
                            board[i][j] += 1     ## 如果 定位 （i，j）周围有-1的话  （i，j）此地的值就 +1
    print()

    for i in range(1, m+1):
        for j in range(1, n+1):
            print("*", end=" ") if board[i][j] == -1 else print(board[i][j], end=" ")
        print()

minesweeper(5, 10, 0.2)