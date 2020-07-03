# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 5:34 PM 4/10/20

"""

class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 10
        self._A = self._make_array(self._capacity)  ###

    def __len__(self):
        return self._n

    def is_empty(self):
        return self._n == 0
    # O(1)
    def __getitem__(self, item):
        if not 0 <= item <= self._n:
            raise ValueError('invalid index')
        return self._A[item]

    # O(1)
    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self.n] = obj
        self._n += 1 ###

    def _make_array(self, c):
        return (c * ctypes.py_object)()   ##########

    def _resize(self, c):
        B = self._make_array(c)   # B的大小为c
        for k in range(self._n):  # 前k个数为A  复制到B
            B[k] = self._A[k]
        self._A = B               # 把大B 赋值给A， A就容量变了
        self._capacity = c        # 改一下capacity

    # O(n)
    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for i in range(self._n, k, -1):      ## 从后往前，最后是 self._n
            self._A[i] = self._A[i-1]        # 前面的数 变成原来后面的数
        self._A[k] = value                   # 插入的第k个 变成value
        self._n += 1

    # O(n)
    def remove(self, value):
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n-1):
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None
                self._n -= 1
                return                   #########
        raise ValueError('Value not found')

    def _print(selfself):
        for i in range(self._n):
            print(self._A[i], end=" ")
        print()


