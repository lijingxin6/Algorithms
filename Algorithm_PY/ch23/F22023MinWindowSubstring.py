# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 5:20 PM 5/25/20

Question: 

"""
import sys
import collections
from collections import Counter

def minWindow(s, t):
    if len(t) > len(s):
        return ""
    lt = len(t)
    count = lt
    ct = collections.Counter(t)
    left = 0
    right = 0
    minLength = sys.maxsize
    notfound = 1
    ansleft = 0
    ansright = 0
    print(ct)
    for i in range(len(s)):
        # found in t
        if ct[s[i]] > 0: # key在T里面
            count -= 1
        ct[s[i]] -= 1
        #print(s[i], ct)
        # found a window, containing all chars from t
        while count == 0: # T中的每个字母都找到了,就找到了一个窗口
            right = i
            notfound = 0
            if right - left < minLength: # 计算window大小
                minLength = right-left
                ansleft = left
                ansright = right
            # when map[left] is 0, meaning the exit char is in t, then count++ 开始缩减窗口
            if ct[s[left]] == 0:
                count += 1 # count变成1  while就不满足了, 说明是invalid窗口,就会跳出while i右移扩大窗口
            ct[s[left]] += 1
            #print("left: ", s[left], ct)
            left += 1
    if notfound == 1:
        return ""
    return s[ansleft:ansright+1]

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))