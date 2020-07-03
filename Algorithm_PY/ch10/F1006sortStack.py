# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 11:47 PM 4/29/20

"""
from ArrayStack import ArrayStack

def sortStack(s):
    r = ArrayStack()

    while not s.is_empty:
        tmp = s.pop()
        while not r.is_empty and tmp < r.top():
            s.push(r.pop())
        r.push(tmp) # 当r是空的 或者 tmp比r最上面的大,可以直接push进去
    return r

