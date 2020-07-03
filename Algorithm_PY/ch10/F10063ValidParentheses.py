# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 9:56 AM 4/30/20

Question: 1006_Ex3

"""

def isValid(s):
    stack = []
    for p in s:
        if(p =='(' or p =='[' or p =='{'):
            stack.append(p)
        else:  # p 不是左括号 ( [ { 的一员
            if len(stack) == 0:
                return False
            if (   (p == ')' and stack[-1] == '(')
                or (p ==']' and stack[-1] == '[' )
                or (p =='}' and stack[-1] == '{')):
                stack.pop()
            else:
                return False
    return len(stack) == 0

s = ""
print(isValid(s))
s = "{}"
print(isValid(s))
s = "{{}}"
print(isValid(s))
s = "{{}}{}{}"
print(isValid(s))
s = "{{{}}{}{{}}}"
print(isValid(s))
s = "[]{}([{}]{})"
print(isValid(s))