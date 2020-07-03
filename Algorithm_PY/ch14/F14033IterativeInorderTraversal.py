# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 5:28 PM 5/7/20

Question: 

"""
from BinarySearchTree import BinarySearchTree
from BinarySearchTree import Node
from F14031IterativeGet import AdvBST1
from F14032IterativeAdd import AdvBST2

class AdvBST3(AdvBST2):
    # # Traversal Methods
    # def print_inorder(self):
    #     self._print_inorder(self._root)
    #     print('')
    #
    # def _print_inorder(self, node):
    #     if (node is None):
    #         return
    #     self._print_inorder(node._left)
    #     print('[', node._item, ']', end=" ")
    #     self._print_inorder(node._right)

    def printInorderIterative(self):
        node = self._root
        stack = []

        while True:
            while (node is not None):  # 退出的时候 说明找到最左下的点了
                stack.append(node)
                node = node._left
            if len(stack) == 0:  # stack为空 退出
                return
            # stack 不为空  pop 及 打印, node往右
            node = stack.pop()
            print('[', node._item, ']', end=" ")
            node = node._right

bst = AdvBST3()
numbers = [6, 4, 8, 7, 9, 2, 1, 3, 5, 13, 11, 10, 12]
for i in numbers:
    bst.add(i)
#bst.print_inorder()
bst.printInorderIterative()