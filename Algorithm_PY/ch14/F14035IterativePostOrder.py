# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 12:14 AM 5/8/20

Question: 

"""
from BinarySearchTree import BinarySearchTree
from BinarySearchTree import Node
from F14031IterativeGet import AdvBST1
from F14032IterativeAdd import AdvBST2
from F14033IterativeInorderTraversal import AdvBST3
from F14034IterativePreOrder import AdvBST4

class AdvBST5(AdvBST4):
    def printPostorderIterative(self):
        node = self._root
        stack = []
        stack.append(node)

        while len(stack) != 0:
            node = stack[-1]
            if node._left is None and node._right is None:
                pop = stack.pop()
                print('[', node._item, ']', end=" ")

            else:
                if node._right is not None:
                    stack.append(node._right)
                    node._right = None
                if node._left is not None:
                    stack.append(node._left)
                    node._left = None
        print('')

    def printPostorderIterative2(self):
        stack = [(self._root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    print('[', node._item, ']', end=" ")
                else:
                    # post-order
                    stack.append((node, True))
                    stack.append((node._right, False))
                    stack.append((node._left, False))

# bst = AdvBST5()
# numbers = [6, 4, 8, 7]
# for i in numbers:
#     bst.add(i)
# bst.print_postorder()
# bst.printPostorderIterative()

bst = AdvBST5()
numbers = [8, 6, 3, 7, 10, 15]
for i in numbers:
    bst.add(i)
bst.printPostorderIterative2()