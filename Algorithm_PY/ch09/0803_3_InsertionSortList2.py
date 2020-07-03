# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 9:38 AM 4/24/20

"""
from util.LinkedList import LinkedList
from util.LinkedList import Node
def insertionSortList(head):
    dummy = Node(0)
    cur = head
    while cur is not None:
        pre = dummy   # 需要一直比较 dummy后面的与cur的值的大小. 所以单独设立一个pre
        while pre.next is not None and pre.next.value < cur.value: # 如果pre后一个值小, pre就后移 继续比较
            pre =pre.next
        temp = cur.next
        cur.next = pre.next
        pre.next = cur
        cur = temp
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


