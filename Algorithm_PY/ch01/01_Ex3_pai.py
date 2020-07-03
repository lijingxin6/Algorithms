# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 10:17 PM 4/9/20

"""
# \frac{\pi}{4} = 1-\frac{1}{3}+\frac{1}{5}-\frac{1}{7}+\frac{1}{9}+…
def pi1(n):
    pi = 0
    sign = 1
    for i in range(1, n+1, 2):
        pi += sign * (1 / i)
        sign *= -1
    return pi * 4

pi1(10000)

# 蒙特卡洛模拟
from random import random
def pi2(TRIES):
    hits = 0
    for i in range(TRIES):
        r = random()
        x = -1 + 2 * r
        r = random()
        y = -1 + 2 * r
        if x * x + y * y <= 1:
            hits += 1
    return  4 * (hits / TRIES)

print(pi2(10000000))