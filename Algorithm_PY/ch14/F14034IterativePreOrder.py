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
class AdvBST4(AdvBST3):
    def printPreorderIterative(self):
        ret = []
        stack = [self._root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node._item)
                stack.append(node._right)
                stack.append(node._left)
        return ret