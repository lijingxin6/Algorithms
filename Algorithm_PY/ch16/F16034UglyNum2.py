# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 4:58 PM 5/12/20

Question: 

"""
import heapq
def nthUglyNumber(n):
    q2, q3, q5 = [2], [3], [5]
    ugly = 1
    for u in heapq.merge(q2, q3, q5):
        if n == 1:
            return ugly
        if u > ugly: # 当前数字比上次的ugly大, 防止取重复的数
            ugly = u
            n -= 1
            q2 += 2 * u, # 每次放三个进去
            q3 += 3 * u,
            q5 += 5 * u,
print(nthUglyNumber(20))