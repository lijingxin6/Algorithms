# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 11:36 PM 4/29/20

"""

class twoStacks:

    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size

    def push1(self, x):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = x
        else:
            print("Stack Overflow")

    def push2(self, x):
        if self.top1 < self.top2 -1:
            self.top2 -= 1
            self.arr[self.top2] = x
        else:
            print("Stack Overflow")

    def pop1(self):
        if self.top1 >=0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            print("Stack Underflow")

    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            print("Stack Underflow")

ts = twoStacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)
print("Popped element from stack1 is ", ts.pop1())
ts.push2(40)
print("Popped element from stack2 is ", ts.pop2())
print("Popped element from stack2 is ", ts.pop2())
print("Popped element from stack2 is ", ts.pop2())
print("Popped element from stack2 is ", ts.pop2())
print("Popped element from stack2 is ", ts.pop2())
print("Popped element from stack2 is ", ts.pop2())
ts.push2(20)
ts.push2(30)
print("Popped element from stack2 is ", ts.pop2())
print("Popped element from stack2 is ", ts.pop2())
print("Popped element from stack2 is ", ts.pop2())