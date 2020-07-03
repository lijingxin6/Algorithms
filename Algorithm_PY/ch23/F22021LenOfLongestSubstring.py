# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 11:22 AM 5/25/20

Question: 

"""
def lengthOfLongestSubstring(s):
    start = maxLength = 0
    usedChar = {} # dict: {key是字母 : value是其idx}

    for i, c in enumerate(s):
        if c in usedChar and start <= usedChar[c]: # 判断当前字母  上一次出现的位置是否在窗口之内
            start = usedChar[c] + 1 # 在窗口之外, start 直接设置成 出现重复字母的 上一次位置的 后面
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChar[c] = i

    return maxLength

def lengthOfLongestSubstring2(s):
    usedChar = set()
    maxLength = 0
    i = j = 0
    n = len(s)
    while (i < n and j < n):
        if s[j] not in usedChar: # 没出现过
            usedChar.add(s[j])
            j += 1
            maxLength = max(maxLength, j - i)
        else:
            usedChar.remove(s[i]) # 在set里出现过, remove s[i] 注意这里是 s[i] 也就是删掉前面的重复数字
            i += 1
    return maxLength
s = 'dxyzabcaxyzlmnbcbb'
lengthOfLongestSubstring2(s)