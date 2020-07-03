# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 10:51 AM 4/30/20

Question: 1006_Ex5

Examples:
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

"""

def decodeString(s):
    stack = []
    stack.append(["", 1])
    num = ""

    for ch in s:
        if ch.isdigit():
            num += ch
        elif ch == '[':
            stack.append(["", int(num)]) # 遇到 [  就把 [ 前面的数字num push进stack,然后num重置
            num = ""
        elif ch ==']': # 一遇到 ]  就把stack pop出最后的元素和次数,
            st, k = stack.pop()
            stack[-1][0] += st * k
        else:  # 遇到字母的情况,直接加到最后一个的元素上
            stack[-1][0] += ch
    return stack[0][0]

s = "3[a]2[bc]"
print(decodeString(s))
s = "3[a2[c]]"
print(decodeString(s))
s = "2[abc]3[cd]ef"
print(decodeString(s))
s = "12[ab]"
print(decodeString(s))