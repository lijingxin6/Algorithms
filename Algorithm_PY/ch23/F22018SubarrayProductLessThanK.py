# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 9:27 PM 5/24/20

Question: 

"""

'''
10, 5, 2, 6
10            Y
10, 5         Y
10, 5, 2      X
    5, 2      Y
    5, 2, 6   Y
'''
def numSubarrayProductLessThanK(nums, k):
    product = 1
    i = 0
    ans = 0
    for j, num in enumerate(nums):
        product *= num
        while product >= k:
            product /= nums[i]
            i += 1
        ans += (j - i + 1)

    return ans

nums = [10, 5, 2, 6]
k = numSubarrayProductLessThanK(nums, 100)
print(k)

nums = [1,5,4,3,6,2,7]
k = numSubarrayProductLessThanK(nums, 100)
print(k)