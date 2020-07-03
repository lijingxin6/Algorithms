# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 7:21 PM 3/24/20

"""

import time
#import matplotlib.pyplot as plt
import random
import math
# matplotlib inline

def random_list(l):
    return [[int(1000*random.random()) for i in range(l * n)] for n in range(1, 20)]


def singing_score(values):
    start = time.time()
    small_pos = 0
    for i in range(1, len(values)):
        if values[i] < values[small_pos]:
            small_pos = i
    high_pos = 0
    for i in range(1, len(values)):
        if values[i] > values[high_pos]:
            high_pos = i
    values.remove(values[small_pos])
    values.remove(values[high_pos])
    score = sum(values) // len(values)
    t = time.time()
    return score, len(values), t


def singing_score2(values):
    start = time.time()
    maxx = values[0]
    minn = values[0]
    summ = values[0]
    for i in range(1, len(values)):
        if values[i] < minn:
            minn = values[i]
        if values[i] > minn:
            maxx = values[i]
        summ += values[i]

    rst = summ / (len(values) - 2)
    t = time.time() - start
    return rst, len(values), t

values =  [8,9,5,10,5,8,7,9,9.5]
v = singing_score(values)
print(v)