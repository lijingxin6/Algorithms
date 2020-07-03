# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 3:19 PM 4/15/20

"""
import numpy as np

def Fibonacci_Matrix_tool(n):
    Matrix = np.matrix('1 1; 1 0')
    if n == 1:
        return Matrix
    if n == 2:
        return pow(Matrix, 2)
    elif n % 2:
        return Fibonacci_Matrix_tool(n//2) ** 2 * Matrix
    else:
        return Fibonacci_Matrix_tool(n//2) ** 2

def Fibonacci_Matrix_tool2(n):
    Matrix = np.matrix('1 1; 1 0')
    return pow(Matrix, n)

def Fibonacci_Matrix(n):
    result_list = []
    for i in range(n):
        result_list.append(np.array(Fibonacci_Matrix_tool2(i))[0][0])
    return result_list

print(Fibonacci_Matrix(5))


def mul(a, b):  # 首先定义二阶矩阵乘法运算
    c = [[0, 0], [0, 0]]  # 定义一个空的二阶矩阵，存储结果
    for i in range(2):  # row
        for j in range(2):  # col
            for k in range(2):  # 新二阶矩阵的值计算
                c[i][j] += a[i][k] * b[k][j]
    return c

def F5(n):
    if n <= 1: return max(n, 0)
    res = [[1, 0], [0, 1]]  # 单位矩阵，等价于1
    A = [[1, 1], [1, 0]]  # A矩阵
    while n:
        if n & 1: res = mul(res, A)  # 如果n是奇数，或者直到n=1停止条件
        A = mul(A, A)  # 快速幂
        n >>= 1  # 整除2，向下取整
    return res[0][1]
