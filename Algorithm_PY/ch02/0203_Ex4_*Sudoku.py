# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 11:23 PM 4/10/20

   _ _ _ _ _ 4 3 2 1      num
   _ _ _ _ _ 3 2 1 0      idx
   4   <==>  1 << 3      3 <==>  1 << 2

"""

def sudoku(matrix):
    n = len(matrix)
    result_row = result_col = result_block = 0

    for i in range(n):
        result_row = result_col = result_block = 0
        for j in range(n):
            # check row
            tmp = matrix[i][j]
            if( ( result_row & (1 << (tmp-1)) ) == 0):        # 只有 1 & 1才执行else， 1 & 1的情况是 已经有这个数了
                result_row = result_row | (1 << (tmp - 1))    # & 之后的结果整体为0，但是 不是每一位都是0，求 或｜ 可以保留matrix的信息 方便下次比较
            else:
                print("row", i, j)
                return False

            # check col
            tmp = matrix[j][i]  # i和j交换下  check col
            if( ( result_col & (1 << (tmp - 1))) == 0 ) :
                result_col = result_col | (1 << (tmp - 1))
            else:
                print("col", j, i)   ##  j 在前  i在后
                return False

            # check block
            idx_row = (i//3) * 3 + j//3   # i=0,j=4  第一行正数第5个  idx_row = 1   第二行
            idx_col = (i%3) * 3 + j%3     # i=0,j=4  第一行正数第5个， idx_col = 1   第二列
            tmp = matrix[idx_row][idx_col]
            if ((result_block & (1 << (tmp - 1)))==0):
                result_block = result_block | (1 << (tmp-1))
            else:
                print("block", idx_row, idx_col)
                return False
    return True

matrix = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]
print(sudoku(matrix))


