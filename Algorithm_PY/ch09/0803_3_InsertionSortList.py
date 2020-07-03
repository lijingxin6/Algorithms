# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 5:14 PM 4/22/20

"""
from util.LinkedList import LinkedList
from util.LinkedList import Node

# O(n^2)
def insertionSortList(head):
    dummy = Node(0)
    cur = head
    # pre is the sorted part
    # when see a new node, start from dummy
    # cur is the unsorted part
    while cur is not None: # 还有元素没有探索过  cur就是新元素  ==> cur 非空 执行, 空 跳出while
        pre = dummy # 每次第一步 先把dummy设置成prev
        while pre.next is not None and pre.next.value < cur.value: # prev.next 比 cur小  prev后移
            pre = pre.next
        temp = cur.next  # 新建一个temp  方便cur后移
        cur.next = pre.next  # cur 连接到 pre.next的那个元素, 断开cur 与temp的连接
        pre.next = cur       # pre.next断开与 prev下一个元素的连接, 连接 cur
        cur = temp           # cur 后移一位到temp
    return dummy.next

node1 = Node(-9)
node2 = Node(1)
node3 = Node(-13)
node4 = Node(6)
node5 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
lst = LinkedList()
lst.head.next = node1
lst.printlist()

node = insertionSortList(node1)

lst.head.next = node
lst.printlist()
