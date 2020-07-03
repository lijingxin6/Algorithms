# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 10:24 AM 5/13/20

Question: 

"""
import heapq
def findMaximizedCapital2(k, W, Profits, Capital):
    current = []
    future = sorted(zip(Capital, Profits))[::-1] # capital排序
    print(future)
    for _ in range(k):
        while future and future[-1][0] <= W:  # afford   需要的启动资金 小于 现在的钱
            heapq.heappush(current, -future.pop()[1]) #minheap 变成maxheap  加上 - 号
        if current:
            W -= heapq.heappop(current)
    return W

k=2
W=0
Profits=[1,2,3]
Capital=[0,1,1]

findMaximizedCapital2(k, W, Profits, Capital)