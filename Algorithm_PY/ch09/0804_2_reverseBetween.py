# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 8:52 PM 4/24/20

    Reverse a linked list from position m to n. Do it in-place and in one-pass.

    For example:

    Given 1->2->3->4->5->NULL, m = 2 and n = 4,

    return 1->4->3->2->5->NULL.

"""
from util.LinkedList import LinkedList
from util.LinkedList import Node

def reverseBetween(head, m, n):
    if m == n:
        return head

    dummyNode = Node(0)
    dummyNode.next = head
    start = dummyNode
    for i in range(m-1):
        start = start.next

    pre = None
    cur = start.next
    for i in range(n-m+1):
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    start.next.next = cur
    start.next = pre
    return dummyNode.next

lst = LinkedList()
lst.add_last(1)
lst.add_last(3)
lst.add_last(5)
lst.add_last(7)
lst.add_last(9)
lst.printlist()
lst.head.next = reverseBetween(lst.head.next, 2, 4)
lst.printlist()
lst.head.next = reverseBetween(lst.head.next, 1, 4)
lst.printlist()
lst.head.next = reverseBetween(lst.head.next, 1, 3)
lst.printlist()

