# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 8:16 PM 4/11/20

====>   Given a set of distinct integers, nums, return all possible subsets

"""

def subsets(nums):
    result = [[]]
    for num in nums:
        for element in result[:]:
            x = element[:]
            x.append(num)
            result.append(x)
    return  result

nums = [1, 2, 3]
subsets(nums)
print(subsets(nums))