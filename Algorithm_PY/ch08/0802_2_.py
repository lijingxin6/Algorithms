# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 5:06 PM 4/20/20

"""
from util.LinkedList import LinkedList
from util.LinkedList import Node

# O(n)
def find_middle(lst):
    assert lst.head is not None and lst.head.next is not None

    head = lst.head
    fast = head
    slow = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow.value

lst = LinkedList()
#find_middle(lst)
lst.add_last(1)
print(find_middle(lst))
lst.add_last(2)
lst.add_last(3)
lst.add_last(4)
print(find_middle(lst))

lst.add_last(5)
print(find_middle(lst))
