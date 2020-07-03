# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 5:58 PM 5/22/20

Question: 

"""


# O(n)
# space: O(n)
def twoSum(nums, target):
    dic = {}
    for i, num in enumerate(nums):
        if num in dic:  # O(1)
            return [dic[num], i] # dic[num]是另一个数的位置, 第二个i是当前数的位置
        else:
            dic[target - num] = i

nums = [1,2,4,7]
target = 6
twoSum(nums,target)