# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 9:54 AM 4/10/20

"""

def mults():
    for i in range(1,10):
        for j in range(1,i+1):
            print(j, "*", i, "=", j*i, end=" ")
        print()

mults()