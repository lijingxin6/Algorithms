# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 11:06 AM 4/14/20

"""
from bisect import bisect
def findRadius(houses, heaters):
    heaters.sort()
    ans = 0

    for h in houses:
        hi = bisect(heaters, h)
        left = heaters[hi - 1] if hi - 1 >= 0 else float('-inf')     # 找到 左 边的供暖设备
        right = heaters[hi] if hi < len(heaters) else float('-inf')  # 找到 右 边的供暖设备
        ans = max(ans, min(h - left, right - h))                     # min 是看 离着左边还是右边最近
                                                                     # max 是看 在所有房子的最近距离  求一个最大值
    return ans
