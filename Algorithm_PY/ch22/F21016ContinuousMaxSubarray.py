# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 9:25 AM 5/24/20

Question: 

"""
from itertools import accumulate  # since Python 3.2:
def max_subarray(numbers, ceiling):
    cum_sum = [0]
    cum_sum = cum_sum + numbers
    cum_sum = list(accumulate(cum_sum))

    l = 0
    r = 1  # two pointers start at tip of the array.
    maximum = 0
    while l < len(cum_sum):
        while r < len(cum_sum) and cum_sum[r] - cum_sum[l] <= ceiling:  # valid + 1个值 => invalid窗口, 停止
            r += 1
        if cum_sum[r - 1] - cum_sum[l] > maximum:  # since cum_sum[0] = 0, thus r always > 0.去掉新加的1个值,
            maximum = cum_sum[r - 1] - cum_sum[l]  # valid窗口 > 全局变量,  更新全局变量
            pos = (l, r - 2)  # cum_sum 比 numbers 多一个0, 所以 r-1的基础上再减1  => r-2
        l += 1  # invalid 要l往右移 直到将它变成valid => 也就是去掉最前面,  valid之后再r往后移
    return pos

a = [4, 7, 12, 1, 2, 3, 6]
m = 15
result = max_subarray(a, m)
result