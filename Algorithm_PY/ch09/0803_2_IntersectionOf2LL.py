# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 8:55 AM 4/24/20

"""
from util.LinkedList import LinkedList
from util.LinkedList import Node

# 方法一: 先获取长度, 假设  长-短= k, 那么长的那个先跑 k步, 再一起跑,直到两个相等
def intersection(headA, headB):
    # 分别得到A B 的长度
    curA, curB = headA, headB
    lenA, lenB = 0, 0
    while curA:
        lenA += 1
        curA = curA.next
    while curB:
        lenB += 1
        curB = curB.next
    # 从头开始
    curA, curB = headA, headB
    if lenA > lenB:
        for i in range(lenA - lenB):
            curA = curA.next
    elif lenB > lenA:
        for i in range(lenB - lenA):
            curB = curB.next
    while curB != curA: # 没相遇 执行, 相遇 跳出while
        curB = curB.next
        curA = curA.next
    return curA

# 方法二: 短的先到终点,到终点后立即返回到长的起点开跑.  长的到终点后立即返回从短的起点开跑. 两者相遇即是共同的起点
def intersection2(headA, headB):
    A, B = headA, headB
    while A != B:
        A = A.next if A else headB
        B = B.next if B else headA
    return A
