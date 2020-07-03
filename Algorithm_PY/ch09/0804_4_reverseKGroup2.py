# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:59 AM 4/25/20

Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

"""
from util.LinkedList import LinkedList
from util.LinkedList import Node
def reverseKGroup(head, k):   # k=2的话就是相当于前一个例题
    if head is None or k < 2:
        return head
    # 找开头 find the first reversed Group's head
    next_head = head
    for i in range(k-1):
        next_head = next_head.next
        if next_head is None:
            return head
    ret = next_head   # 作为整个LL的开头

    # reverse
    cur = head   # 开头
    while next_head:
        tail = cur   # 第一组的结尾
        pre = None

        for i in range(k):
            if next_head:
                next_head = next_head.next  # 1. 为了tail.next备用   2.为了判断 while循环

            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        tail.next = next_head or cur # 第一组结尾 + 第二组开头   第二组开头有两种情况 用or得到
    return ret

lst = LinkedList()
lst.add_last(1)
lst.add_last(3)
lst.add_last(5)
lst.add_last(7)
lst.add_last(9)
lst.printlist()
lst.head.next = reverseKGroup(lst.head.next, 2)
lst.printlist()
lst.head.next = reverseKGroup(lst.head.next, 3)
lst.printlist()
lst.head.next = reverseKGroup(lst.head.next, 4)
lst.printlist()
lst.head.next = reverseKGroup(lst.head.next, 5)
lst.printlist()
lst.head.next = reverseKGroup(lst.head.next, 7)
lst.printlist()