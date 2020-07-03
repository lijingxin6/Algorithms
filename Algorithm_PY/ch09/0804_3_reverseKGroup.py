# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 9:54 AM 4/25/20
    Swap Nodes in Pairs

    Given a linked list, swap every TWO adjacent nodes and return its head.

    For example,

    Given 1->2->3->4, you should return the list as 2->1->4->3.

    Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""
from util.LinkedList import LinkedList
from util.LinkedList import Node
def swapPairs(head):
    dummy = cur = Node(0)
    cur.next = head

    while cur.next and cur.next.next:  # 从head 和 head的下一个 开始
        p1 = cur.next
        p2 = cur.next.next

        p1.next = p2.next  # p1 在 p2 前变化
        p2.next = p1
        cur.next = p2

        # cur.next = p2
        # p1.next = p2.next
        # p2.next = p1

        cur = cur.next .next
    return dummy.next

lst = LinkedList()
lst.add_last(1)
lst.add_last(2)
lst.add_last(3)
lst.add_last(4)
lst.printlist()
lst.head.next = swapPairs(lst.head.next)
lst.printlist()
lst.head.next = swapPairs(lst.head.next)
lst.printlist()
