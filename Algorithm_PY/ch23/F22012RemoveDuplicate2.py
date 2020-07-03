# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 9:40 AM 5/24/20

Question: 排序数组 删除重复的数, 重复最多2次

"""
def removeDuplicates2(nums):
    count = 0
    for i in range(len(nums)):
        if count < 2 or nums[count - 2] != nums[i]:
            nums[count] = nums[i]
            count += 1
    return count
nums = [1,1,1,2,2,3,3,3,5]
print(removeDuplicates2(nums))