# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 10:29 AM 5/10/20

Question: 

"""
from BinarySearchTree import BinarySearchTree
from BinarySearchTree import Node

class AdvBST2(BinarySearchTree):

    def levelOrder(self):
        if not self._root:
            return []
        ans, level = [], [self._root]
        while level:
            ans.insert(0, [node._item for node in level])
            temp = []
            for node in level:
                temp.extend([node._left, node._right])
            level = [leaf for leaf in temp if leaf]

        return ans

    def levelOrder2(self):
        if not self._root:
            return []
        ans, level = [], [self._root]
        while level:
            ans.append([node._item for node in level])
            temp = []
            for node in level:
                temp.extend([node._left, node._right])
            level = [leaf for leaf in temp if leaf]
        ans.reverse()
        return ans
