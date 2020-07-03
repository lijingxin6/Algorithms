# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 5:54 PM 4/12/20

"""

def _bubble_sort(nums: list, reverse=False):
    for i in range(len(nums)):
        for j in range(len(nums) - 1 - i):
            if(nums[j] > nums[j+1]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    if reverse:
        nums.reverse()
    return len(nums)

def bubble_sorted(nums: list, reverse=False) -> list:
    nums_copy = list(nums)  ##
    _bubble_sort(nums_copy, reverse=reverse)
    return nums_copy

l = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
l = bubble_sorted(l, reverse=True)
print(l)

def bubble_sort_mod(array):
    for i in range(len(array)):
        for j in range(1, len(array) - i):   #
            if array[j] < array[j - 1]:
                array[j], array[j-1] = array[j-1], array[j]  # put the larger back
                is_sorted = False
        if (is_sorted): break
    return len(array)

