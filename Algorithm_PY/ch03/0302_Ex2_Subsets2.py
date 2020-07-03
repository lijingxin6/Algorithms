# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 9:13 AM 4/12/20

====>  Given a collection of integers that might contain duplicates, nums, return all possible subsets.

"""

def subsets2(nums):
    res = [[]]
    for num in nums:
        res += [ i+[num] for i in res if i+[num] not in res ]
    return res

def subsets2_recursive(nums):
    lst = []
    result = []
    nums.sort()
    print(nums)
    subsets2_recursive_helper(result, lst, nums, 0)
    return result

def subsets2_recursive_helper(result, lst, nums, pos):
    result.append(lst[:])
    for i in range(pos, len(nums)):
        if(i!= pos and nums[i] == nums[i-1]):     ### 剪枝 i != pos 为了防止第一次出现 1 就被剪枝了 ==》 pos=1， i=1 不能执行
            continue                              ### 且保证 pos=0， i=1 时 能 执行剪枝操作
        lst.append(nums[i])
        subsets2_recursive_helper(result, lst, nums, i+1)
        lst.pop()
nums = [1, 2, 3, 1]
print(subsets2_recursive(nums))9