# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 10:54 PM 4/10/20

"""

def magic_square(n):
    magic = [[0] * (n) for i in range(n)]
    row = n - 1
    col = n // 2
    magic[row][col] = 1  ## 把 最后一行最中间的数字设置成 1

    for i in range(2, n*n + 1):
        try_row = (row + 1) % n
        try_col = (col + 1) % n

        if magic[try_row][try_col] == 0 :
            row = try_row
            col = try_col
        else:                         # != 0 , 意味着下一个位置已经有数了，需要位置往上一行
            row = (row - 1 + n) % n   # +n是为了保证是正数，  同一列 不同行，所以不需要col

        magic[row][col] = i
    for x in magic:
        print(x, sep=" ")

magic_square(3)
