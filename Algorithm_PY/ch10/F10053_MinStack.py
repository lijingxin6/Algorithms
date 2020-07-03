# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 5:03 PM 4/29/20

"""

import sys
from ArrayStack import ArrayStack

class MinStack(ArrayStack):

    def __init__(self):
        super().__init__()

    def push(self, v):  # self 传递的是实例对象
        newMin = min(v, self.min())  # 获取最小值
        super(MinStack, self).push(NodeWithMin(v, newMin))  # 将 v 和 最小值 作为pair 一起push进去

    def min(self):
        if (super().is_empty()):
            return sys.maxsize
        else:
            return super().top()._min

class NodeWithMin:
    def __init__(self, v, min):
        self._value = v
        self._min = min

# minStack = MinStack()
# minStack.push(4)
# minStack.push(6)
# minStack.push(8)
# minStack.push(3)
# print(minStack.min())
# minStack.pop()
# minStack.pop()
# print(minStack.min())

class MinStack2(ArrayStack):

    def __init__(self):
        super().__init__() #         self._data = []
        self.min_stack = ArrayStack() # self包含 min_stack

    def push(self, v):
        if v <= self.min(): # v与min_stack里最小的进行比较, 如果v比min还小,就执行下一步
            self.min_stack.push(v) # 把最小的放进 self 的 min_stack
        super().push(v)            # 把所有的放进 self 去
        return v


    def min(self):
        if self.min_stack.is_empty():
            return sys.maxsize
        else:
            return self.min_stack.top()

    def pop(self):
        v = super().pop()
        if v == self.min(): # 如果 v是min的, min_stack 也一并进行pop
            self.min_stack.pop()
        return v
minStack = MinStack2()
minStack.push(4)
minStack.push(6)
minStack.push(8)
minStack.push(3)
print(minStack.min())
minStack.pop()
minStack.pop()
print(minStack.min())




