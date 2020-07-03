# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 4:57 PM 4/24/20

"""
from util.LinkedList import LinkedList
from util.LinkedList import Node
def reverse(lst):
    head = lst.head
    pre = None
    cur = head.next
    temp = None

    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    head.next = pre

lst = LinkedList()
lst.add_last(1)
lst.add_last(3)
lst.add_last(5)
lst.add_last(7)
lst.add_last(9)
lst.printlist()
reverse(lst)
lst.printlist()