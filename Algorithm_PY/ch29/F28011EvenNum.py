# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 9:29 AM 5/31/20

Question: Number of Even Substrings

"""

def evenNum(s):
    count = 0
    count0 = 0
    for i in range(len(s)):
        if int(s[i]) == 0:
            count0 += 1
        if int(s[i]) % 2 == 0:
            count += i + 1
    return count - count0

print(evenNum("12034"))