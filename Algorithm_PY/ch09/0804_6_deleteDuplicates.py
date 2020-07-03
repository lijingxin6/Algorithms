# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 12:54 PM 4/25/20

"""

from util.LinkedList import LinkedList
from util.LinkedList import Node

# 删除到只留一个 Given 1->1->2->3->3, return 1->2->3.
def deleteDuplicates(head):
    if head == None:
        return head
    node = head

    while node.next: # node.next 存在执行,  不存在 跳出
        if node.value == node.next.value:
            node.next = node.next.next
        else:
            node = node.next
    return head

# 删除所有重复的,一个不留 Given 1->1->1->2->3, return 2->3.
def deleteDuplicates2(head):
    dummy = pre = Node(0) # dummy 留着作为开头连接后面,   pre去连接后面的
    dummy.next = head # dummy和LL连接起来

    while head and head.next:
        if head.value == head.next.value:
            while head and head.next and head.value == head.next.value:
                head = head.next
            head = head.next
            pre.next = head
        else:
            pre = pre.next
            head = head.next
    return dummy.next


lst = LinkedList()
lst.add_last(1)
lst.add_last(3)
lst.add_last(3)
lst.add_last(3)
lst.add_last(5)
lst.add_last(7)
lst.add_last(7)
lst.add_last(9)
lst.head.next = deleteDuplicates2(lst.head.next)
lst.printlist()