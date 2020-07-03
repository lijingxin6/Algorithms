# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 2:10 PM 4/24/20

"""
from util.LinkedList import LinkedList
from util.LinkedList import Node
def sortList(head):
    if head is None or head.next is None:
        return head
    mid = getMiddle(head)
    rhead = mid.next
    mid.next = None
    return merge(sortList(head), sortList(rhead))


def merge(lhead, rhead):
    dummyNode = dummyHead = Node(0)
    while lhead and rhead: # lhead 和 rhead非空 执行, 任意一个空, 跳出while
        if lhead.value < rhead.value:
            dummyHead.next = lhead
            lhead = lhead.next
        else:
            dummyHead.next = rhead
            rhead = rhead.next
        dummyHead = dummyHead.next
    if lhead: # rhead空, lhead非空
        dummyHead.next = lhead
    elif rhead: # lhead空  rhead非空
        dummyHead.next = rhead
    return dummyNode.next


def getMiddle(head):
    if head is None:
        return head
    slow = fast = head
    while fast.next and fast.next.next:    # 条件: fast.next.next
        slow = slow.next
        fast = fast.next.next
    return slow

node1 = Node(9)
node2 = Node(1)
node3 = Node(13)
node4 = Node(6)
node5 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node = sortList(node1)
lst = LinkedList()
lst.head.next = node
lst.printlist()