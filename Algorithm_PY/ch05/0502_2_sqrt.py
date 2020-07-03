# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 3:13 PM 4/14/20

"""

def sqrt(x):
    if x == 0 :
        return 0
    left, right =1, x                     # 上 下 限
    while(left <= right):
        mid = left + (right - left) // 2  # 中间值
        if(mid = x // mid):
            return mid
        if(mid < x // mid):
            left = mid + 1
        else:
            right = mid + 1
    return right             # return right