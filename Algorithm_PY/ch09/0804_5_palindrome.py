# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 12:35 PM 4/25/20

"""
from util.LinkedList import LinkedList
from util.LinkedList import Node
def isPalindrome(head):
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.value == slow.value: # 满足条件  slow往后移一个, rev往前移一个
        slow = slow.next
        rev = rev.next
    return not rev

lst = LinkedList()
lst.add_last(1)
lst.add_last(3)
lst.add_last(5)
lst.add_last(7)
lst.add_last(9)
lst.printlist()
print(isPalindrome(lst.head.next))
lst.printlist()