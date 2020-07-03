# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 5:24 PM 4/12/20

"""

# recursive
def bi_search_re(num_list, val):
    def bi_search(l, h):
        if(l > h):
            return -1
        mid = (l + h) // 2
        if (num_list[mid] == val):
            return mid
        elif num_list[mid] > val:
            return bi_search(l, mid-1)  # mid - 1
        else:
            return bi_search(mid+1, h)  # mid + 1
    return bi_search(0, len(num_list))

num_list = [1,2,3,5,7,8,9]
print(bi_search_re(num_list, 4))
print(bi_search_re(num_list, 7))

# iterative     !!! 常用 !!!
def bi_search_iter(alist, item):
    left, right = 0, len(alist) - 1   ### right = len(alist) - 1  right是坐标idx， 最大是 len-1
    while(left <= right):
        mid = left + (right - left) // 2
        if alist[mid] == item:
            return mid
        elif alist[mid] > item:
            right = mid -1
        else:
            left = mid + 1
    return -1

num_list = [1,2,3,5,7,8,9]
print(bi_search_iter(num_list, 4))
print(bi_search_iter(num_list, 7))