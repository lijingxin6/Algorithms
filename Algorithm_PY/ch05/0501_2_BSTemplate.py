# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 5:06 PM 4/13/20

"""

def binarysearch(alist, item):
    if len(alist) == 0:
        return -1
    left, right = 0, len(alist) - 1
    while(left + 1 < right):                 # 跳出循环的条件：  LR     LR指向同一个    RL
        mid = left + (right - left) // 2
        if alist[mid] == item:
            right = mid                      # 因为是排好序的， 找第一个的话肯定在mid前面，所以 right=mid
        elif alist[mid] < item:
            left = mid
        elif alist[mid] > item:
            right = mid

    # 跳出循环了， 所以是上面的3个条件
    if alist[left] == item:
        return left
    if alist[right] == item:
        return right
    return -1
