# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 3:37 PM 5/23/20

Question: 

"""
import bisect
def findClosestElements(alist, k, x):
    left = right = bisect.bisect_left(alist, x)
    while right - left < k:
        if left == 0: return alist[:k] # 说明第一个数字就比我小, 后面k个就是想要的
        if right == len(alist): return alist[-k:] # 最后k个就是想要的
        if x - alist[left - 1] <= alist[right] - x: left -= 1
        else: right += 1
    return alist[left:right]


nums = [1, 8, 15, 30, 38, 40, 54]
target = 32
print(findClosestElements(nums, 5, target)) # 找到 5 个 离着target最近的数