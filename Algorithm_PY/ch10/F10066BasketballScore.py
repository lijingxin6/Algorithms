# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 2:53 PM 4/30/20

Question: 1006_Ex6

"""
def calPoints(scores):
    stack = []
    for score in scores:
        if score == '+':
            stack.append(stack[-1] + stack[-2])
        elif score == 'C':
            stack.pop()
        elif score == 'D':
            stack.append(stack[-1] * 2)
        else:
            stack.append(int(score))
    return sum(stack)

scores = ["5", "2", "C", "D", "+"]
print(calPoints(scores))
