# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 4:11 PM 4/28/20

"""

def nextGreat2(nums):
    stack, r = [], [-1] * len(nums) # stack 存放index  stack[-1]是当前最小值
    for i in range(len(nums)):
        while stack and (nums[stack[-1]] < nums[i]): # 第一个大于最小值的为 nums[i]  <=> current num
            r[stack.pop()] = nums[i]   # 最小值的index pop出来, 赋值为 current num
        stack.append(i)
    print(r)
    for i in range(len(nums)): # 在整个nums里找到大于stack[-1]的值
        while stack and (nums[stack[-1]] < nums[i]):
            r[stack.pop()] = nums[i]
        if stack == []:
            break
    return r

array = [37, 6, 4, 5, 2, 25,48]
nextGreat2(array)