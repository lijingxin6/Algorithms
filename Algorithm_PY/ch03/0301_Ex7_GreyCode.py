# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 8:15 PM 4/11/20

"""

def moves(n):
    if n == 0:
        return
    moves(n-1)
    print(n)
    moves(n-1)

# print(moves(3))

def moves_ins(n, forward):
    if n == 0:
        return
    moves_ins(n-1, True)
    print("enter ", n) if forward else print("exit ", n)
    moves_ins(n-1, False)

print(moves_ins(3, True))