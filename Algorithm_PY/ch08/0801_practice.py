# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 10:09 AM 4/20/20

"""
from util.Empty import Empty
from util.Outbound import Outbound

class Node:
    # value
    # next
    def __init__(self, value = None, next = None):  # node的next可能是空的 value 也可以为空
        # data member
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()  # Node的optional  都用的none   head 包括 value 和 next
        self.size = 0
    # O(1)
    def add_first(self, value):
        node = Node(value, None) # 此时还没有next
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    # O(n)
    def add_last(self,value):
        new_node = Node(value)
        node = self.head
        while node.next != None:
            node = node.next
        node.next = new_node
        self.size += 1
    # O(1)
    def remove_first(self):  # to do
        if not self.head.next:
            raise ValueError
        value = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return value

    # O(n)
    def remove_last(self):  # to do
        if not self.head.next:
            raise ValueError
        node = self.head.next
        prev = self.head
        while node.next != None:
            prev = node
            node = node.next
        prev.next = None
        self.size -= 1
        return node.value

    # O(n)
    def insert_at(self, value, index):   # to do
        if(index < 0 or index > self.size):
            raise ValueError
        if not self.head.next:
            raise ValueError
        new_node = Node(value)
        node = self.head
        for i in range(index):
            node = node.next
        new_node.next = node.next  # 先后面
        node.next = new_node       # 在前面
        self.size += 1

    # O(n)
    def romove_at(self, index):
        if (index < 0 or index > self.size):
            raise ValueError
        if not self.head.next:
            raise ValueError
        node = self.head
        for i in range(index):
            node = node.next
        node.next.next = None
        node.next = node.next.next
        self.size -= 1


    # O(n)
    def print_list(self):
        node = self.head
        while node.next != None:  # 第一个node.next -> 8, print 8.  第二个node.next -> 5 print 5
            node = node.next
            print(node.value, end=" ")
        print()

    def length(self):
        return self.size

ll = LinkedList()
ll.add_first(5)
ll.add_first(8)
print(ll.length())
ll.print_list()