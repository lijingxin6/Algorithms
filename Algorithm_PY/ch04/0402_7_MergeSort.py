# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 11:25 AM 4/13/20

"""

def _merge(a: list, b: list) -> list:
    c =[]
    while(len(a) > 0 and len(b) > 0):
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

def _merge_sorted(nums: list) -> list:
    if len(nums) <= 1:
        return nums
    m = len(nums) // 2
    a = _merge_sorted(nums[:m])
    b = _merge_sorted(nums[m:])
    return _merge(a, b)

def merge_sorted(nums: list, reverse=False) -> list:
    nums = _merge_sorted(nums)
    if reverse:
        nums = nums[::-1]
    return  nums

l = [1, 7, 3, 4, 5, 6, 2, 8, 9, 0]
l = merge_sorted(l, reverse=True)
print(l)