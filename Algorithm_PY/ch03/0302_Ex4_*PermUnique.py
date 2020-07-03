# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 1:14 PM 4/12/20

"""
# i=0, 2 [2,3] --> [2,2] 3 和 [2,3] 2 --> [2,2,3] [2,3,2]
# i=1, 剪枝
# i=2， 3 [2,2] --> i=0 [3,2] 2 ，   i=1剪枝 ==》 [3,2,2]
def permUnique(result, nums):
    nums.sort()
    if (len(nums) == 0):
        print(result)
    for i in range(len(nums)):
        if(i != 0 and nums[i] == nums[i-1]):  # i=0的时候不剪枝
            continue
        permUnique(result + str(nums[i]), nums[:i] + nums[i+1:])

nums = [2, 2, 3]
print( permUnique(' ', nums) )




def permuteUnique(nums):
    ans = [[]]
    for n in nums:
        new_ans = []
        for an in ans:
            for i in range(len(an) + 1):
                new_ans.append(an[:i] + [n] + an[i:])
                if i < len(an) and an[i] ==n: break      ##
        ans = new_ans
    return ans
nums = [2, 3, 2]
print( permuteUnique(nums) )