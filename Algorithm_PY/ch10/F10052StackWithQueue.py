# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 4:01 PM 4/29/20

"""
from LinkedList import LinkedList
from LinkedList import Node
from ArrayStack import ArrayStack

class StackWithQueue:

    def __init__(self):
        self.queue = LinkedList()

    def push(self, x):
        self.queue.add_last(x)

    # pop 要把  将要pop的元素x  前面的  所有元素  加入x后面
    def pop(self):
        size = self.queue.size()
        for i in range(1,size):
            self.queue.add_last(self.queue.remove_first())
        self.queue.remove_first()

    def top(self):
        size = self.queue.size()
        for i in range(1,size):
            self.queue.add_last(self.queue.remove_first())
        result = self.queue.remove_first() # 要返回的结果
        self.queue.add_last(result)
        return result


stack = StackWithQueue()
stack.push(1)
stack.push(2)
print(stack.top())

stack = StackWithQueue()
stack.push(1)
stack.push(2)
stack.pop()
stack.push(3)
print(stack.top())
