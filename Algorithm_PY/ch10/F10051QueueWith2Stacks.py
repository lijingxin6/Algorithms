# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 11:23 AM 4/29/20

"""

class QueueWithTwoStacks:

    def __init__(self):
        self.interstack = []
        self.popstack = []

    # O(1)
    def enqueue(self, x):
        self.interstack.append(x)
        return x

    # O(1)
    def dequeue(self):
        if len(self.interstack) == 0 and len(self.popstack) ==0:
            return None
        if len(self.popstack) == 0:
            while len(self.interstack) != 0:
                self.popstack.append(self.interstack.pop())
        return self.popstack.pop()


mystack = QueueWithTwoStacks()
e = mystack.enqueue(3)
print(e)
e = mystack.enqueue(2)
print(e)
e = mystack.enqueue(1)
print(e)
e = mystack.dequeue()
print(e)
e = mystack.dequeue()
print(e)