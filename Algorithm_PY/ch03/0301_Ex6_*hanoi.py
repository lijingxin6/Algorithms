# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 8:00 PM 4/11/20

"""

def hanoi(n, start, end, by):
    if(n == 1):
        print("Move from " + start + " to " + end)
    else:
        hanoi(n-1, start, by, end)
        hanoi(1, start, end, by)     # start --> end
        hanoi(n-1, by, end, start)

n = 3
print(hanoi(n, "longest", "tiny", "medium"))
