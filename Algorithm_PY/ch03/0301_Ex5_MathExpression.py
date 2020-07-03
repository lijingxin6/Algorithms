# -*- coding:utf-8 -*-
"""

author: lijingxin

Created on 7:44 PM 4/11/20

Given two integers a ≤ b, write a program that transforms a into b

by a minimum sequence of increment (add 1) and unfolding (multiply by 2) operations.

For example,

23 = ((5 * 2 + 1) * 2 + 1)

113 = ((((11 + 1) + 1) + 1) * 2 * 2 * 2 + 1)

"""

def intSeq(a, b):
    if(a == b):
        return str(a)
    if(b % 2 == 1):
        return "(" + intSeq(a, b-1) + " + 1 )"
    if(b < 2 * a):
        return "(" + intSeq(a, b-1) + " + 1 )"
    return  intSeq(a, b/2) + " * 2"   # b > 2a

a = 11
b = 113
print(str(b) + "=" + intSeq(a,b))