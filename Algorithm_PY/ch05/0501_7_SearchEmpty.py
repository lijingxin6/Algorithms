# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 9:45 PM 4/13/20

"""

def search_empty(alist, target):
    if len(alist) == 0:
        return -1
    left, right = 0, len(alist) - 1
    while(left + 1< right):
        while(left + 1 < right and alist[right] == ""):    # 从右边开始找 找到第一个非空字符串
            right -= 1
        if (alist[right] == ""):
            right -= 1
        if right < left:
            return -1

        mid = left + (right - left) // 2

        while(alist[mid] == ""):               # 中间为空字符串，mid会后移
            mid += 1
        if alist[mid] == target:
            return mid
        if alist[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if alist[left] == target:
        return left
    if alist[right] == target:
        return right

    return -1

l = ["", "", "", "", 1,"", "", "", "", 2,"", "", 3, "","", "", "", 4,"",""]
print(search_empty(l, 3))