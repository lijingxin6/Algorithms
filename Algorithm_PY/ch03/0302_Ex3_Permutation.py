# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 10:22 AM 4/12/20

"""
# i=0 ==> 1, [2 3]  --> [1,2] 3 和 [1,3] 2  --> [1,2,3]  [1,3,2]
# i=1 ==> 2, [1,3]  --> [2,1] 3 和 [2,3] 1  --> [2,1,3]  [2,3,1]
# i=2 ==> 3, [1,2]  --> [3,1] 2 和 [3,2] 1  --> [3,1,2]  [3,2,1]
def perm(result, nums):
    if (len(nums) == 0):
        print(result)
    for i in range(len(nums)):
        perm(result + str(nums[i]), nums[:i] + nums[i+1:])

nums = [1, 2, 3]
print(perm(' ', nums))

# 1 -> 2 1 , 1 2  --> 3 2 1, 2 3 1, 2 1 3,   3 1 2, 1 3 2, 1 2 3
def permute(nums):
    perms = [[]]
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in range(len(perm) + 1): # 表示 有 len(perm)+1 个选择
                new_perms.append(perm[:i] + [n] + perm[i:])
        perms = new_perms
    return perms

nums = [1, 2, 3]
print(permute(nums))