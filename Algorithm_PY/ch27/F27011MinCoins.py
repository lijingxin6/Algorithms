# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 4:10 PM 5/29/20

Question: 

"""
def minCoins(V):
    available = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    result = []
    for i in available[::-1]:
        while(V>=i):
            V %= i
            result.append(i)

    return result

def minCoins2(V):
    available = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    result = []
    for i in available[::-1]:
        while (V >= i):
            V -= i
            result.append(i)

    return result

V = 93
print(minCoins(V))