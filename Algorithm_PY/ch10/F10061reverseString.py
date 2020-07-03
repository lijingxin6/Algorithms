# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 9:36 AM 4/30/20

"""
from LinkedList import LinkedList
from LinkedList import Node
from ArrayStack import ArrayStack

def reverse(s):
    lst = []
    for i in s:
        lst.append(i)
    result = []
    while len(lst) != 0:
        result.append(lst.pop())
    return ''.join(result)

s = "hello world"
print(reverse(s))

s = "madamimadam"
print(reverse(s))