# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 9:30 PM 4/13/20

"""

def search_range(alist, target):
    if(len(list) == 0):
        return (-1, -1)
    lbound, rbound = -1, -1

    # search for LEFT bound
    left, right = 0, len(alist)-1
    while(left + 1 < right):
        mid = left + (right - left) // 2
        if alist[mid] == target:
            right = mid                 ###
        elif alist[mid] < target:
            left = mid
        else:
            right = mid

    if alist[left] == target:
        lbound = left
    elif alist[right] == target:
        lbound = right
    else:
        return (-1, -1)

    # search for RIGHT bound
    left, right = 0, len(alist) - 1
    while (left + 1 < right):
        mid = left + (right - left) // 2
        if alist[mid] == target:
            left = mid                ###
        elif alist[mid] < target:
            left = mid
        else:
            right = mid

    if alist[left] == target:
        rbound = left
    elif alist[right] == target:
        rbound = right
    else:
        return (-1, -1)
    return (lbound, rbound)
