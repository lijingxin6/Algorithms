# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 5:20 PM 4/13/20

 =====> Find Min in Rotated 【 Sorted 】 Array

"""

def search(alist):
    if len(alist) == 0:
        return -1
    left, right = 0, len(alist) - 1
    while(left + 1 < right):
        if(alist[left] < alist[right]):     # 整体排好序了
            return alist[left]
        mid = left + (right - left) // 2
        if(alist[mid] > alist[left]):       # 前半部分拍好了， 去后半部分找
            left = mid + 1
        else:                              # 后半部分找不到 去前半部分找
            right = mid
    return alist[left] if alist[left] < alist[right] else alist[right]  # 不满足while条件了 LR  返回 LR 较小的那个

l = [3,4,4,5,6,1,1,2]
print(search(l))