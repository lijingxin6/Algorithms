# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 9:30 PM 5/30/20

Question: 

"""
def absoluteA(a):
    mask = a >> 31
    result = (a + mask) ^ mask
    return result


print(absoluteA(0))
print(absoluteA(5))
print(absoluteA(-5))