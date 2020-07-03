# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 11:26 AM 4/13/20

"""

def _quick_sorted(nums: list) -> list:
    if (len(nums) <= 1):
        return nums
    pivot = nums[0]
    left_nums  = _quick_sorted([x for x in nums[1:] if x < pivot])
    right_nums = _quick_sorted([x for x in nums[1:] if x >= pivot])   #     >=
    return left_nums + [pivot] + right_nums


def quick_sort(nums: list, reverse=False) -> list:
    nums = _quick_sorted(nums)
    if reverse:
        nums = nums[::-1]
    return nums, len(nums)

l = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(quick_sort(l))