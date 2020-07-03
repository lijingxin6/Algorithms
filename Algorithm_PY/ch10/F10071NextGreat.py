# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 4:01 PM 4/30/20

Question: 

"""
from LinkedList import LinkedList
from LinkedList import Node
from ArrayStack import ArrayStack

def nextGreat(nums):
    if len(nums) == 0:
        return None
    stack = []
    stack.append(nums[0]) # 第一个栈顶

    for i in range(1,len(nums)):
        while stack and nums[i] > stack[-1]: # 找到第一个大于栈顶的数, 立即pop
            num = stack.pop()
            print(num, ": ", nums[i])
        stack.append(nums[i]) # pop 一个  push一个
    while stack:
        print(stack.pop(), ": -1")

# array = [6, 4, 5, 2, 25]
# print(nextGreat(array))


def nextGreat2(nums):
    if len(nums) == 0:
        return None
    stack, r = [], [0] * len(nums)
    stack.append(0)
    for i in range(1, len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            r[stack.pop()] = nums[i]
        stack.append(i)
    while stack:
        r[stack.pop()] = -1
    return r

array1 = [6, 4, 5, 2, 25]
array2 = [6, 4, 5, 2, 25,4]
array3 = [6, 4, 5, 2, 25,4,5]
print(nextGreat2(array1))
print(nextGreat2(array2))
print(nextGreat2(array3))