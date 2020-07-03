# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 5:46 PM 5/13/20

Question: 

"""

a = [[1],[2],[3],[4]] * 4
print(a)
print(id(x) for x in a)
# print([ [id(y) for y in x] for x in a])
a[0][0] = 9
print(a)
print(id(x) for x in a)

# print([ [id(y) for y in x] for x in a])

# b = a[:]
# b[0][0] = 9
# print(b)
