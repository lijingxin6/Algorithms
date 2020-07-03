# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 8:21 PM 4/13/20

"""

def search_insert_position(alist, target):
    if len(alist) == 0:
        return -1
    left, right = 0, len(alist) - 1
    while(left + 1 < right):
        mid = left + (right - left)//2
        if alist[mid] == target:
            return mid

        if alist[mid] > target:
            right = mid
        else:
            left = mid

        if alist[left] >= target:     #   >=
            return left
        if alist[right] >= target     #   >=
            return right
    return right + 1                   # 都不是 放在最后