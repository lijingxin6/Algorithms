# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 3:40 PM 4/24/20

"""
from util.LinkedList import LinkedList
from util.LinkedList import Node
def partitionList(head, x):
    left_head = Node(None)
    right_head = Node(None)
    left = left_head
    right = right_head
    while head:  # 从head开始, head不为空 -> 执行,  head空 ->跳出
        if head.value < x: # < x 的值
            left.next = head  # 第一次是 连接 None -> head
            left = left.next
        else:    # >= x 的值
            right.next = head
            right = right.next
        head = head.next
    right.next = None
    left.next = right_head.next
    return left_head.next
#head = 1->4->3->2->5->2, x = 3
node1 = Node(1)
node2 = Node(4)
node3 = Node(3)
node4 = Node(2)
node5 = Node(5)
node6 = Node(2)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node = partitionList(node1, 3)
lst = LinkedList()
lst.head.next = node
lst.printlist()