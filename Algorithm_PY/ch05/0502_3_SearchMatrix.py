# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 4:27 PM 4/14/20
  ===> 杨氏搜索
    在一个 m 行 n 列二维数组中， 每一行都按照从左到右递增的顺序排序每一列照从上到下递增的顺序排序。
    请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整

    实现思路：
        如果查找的数字小于最小的或者大于最大的即返回找不到
        从右上角开始检查，范围逐步往下缩减
        当这个数大于目标值则剔除该行
        当这个数小于目标值说明不在此列

"""

# def find_num(nums, target):
#     m = len(nums)
#     n = len(nums[0])
#     if target < nums[0][0] or target > nums[m-1][n-1]:
#         return False
#     i, j = 0, n-1
#     while(i<m or j>=0):
#         if target == nums[i][j]:
#             return (i,j)
#         elif target > nums[i][j]:
#             i += 1
#             continue
#         elif target < nums[i][j]:
#             j -= 1
#             continue
#     return False

def findNumberIn2DArray2(matrix, target):
    if not matrix: return False
    i, j = 0, len(matrix[0])-1
    while i < len(matrix) and j >= 0:
        if target < matrix[i][j]:
            j -= 1
        elif target > matrix[i][j]:
            i += 1
        else:
            return True
    return False

def findNumberIn2DArray(matrix, target):
    if not matrix: return False
    i, j = 0, len(matrix)-1
    while(i < len(matrix) and j >= 0):
        if target > matrix[i][j]:
            i += 1
        elif target < matrix[i][j]:
            j -= 1
        else:
            return True
    return False


if __name__ == "__main__":
    nums = [[1,4,7,11,15], [2,5,8,12,19], [3,6,9,16,22], [10,13,14,17,24], [18,21,23,26,30]]
    print(findNumberIn2DArray(nums, target=22))

