# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 5:27 PM 5/7/20

Question: 

"""
from BinarySearchTree import BinarySearchTree
from BinarySearchTree import Node


class AdvBST1(BinarySearchTree):

    def getIterative(self, key):
        node = self._root
        while (node is not None):
            if key == node._item:
                return node._item
            if key < node._item:
                node = node._left
            else:
                node = node._right
        return None

bst = AdvBST1()
numbers = [6, 4, 8, 7, 9, 2, 1, 3, 5, 13, 11, 10, 12]
for i in numbers:
    bst.add(i)
bst.print_inorder()
bst.getIterative(5)