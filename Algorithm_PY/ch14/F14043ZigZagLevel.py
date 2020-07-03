# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 10:29 AM 5/10/20

Question: 

"""

from F14042LevelOrderTraversal import AdvBST2
class AdvBST3(AdvBST2):

    def zigzagLevelOrder(self, ):
        if not self._root:
            return []
        res, temp, stack, flag = [], [], [self._root], 1
        while stack:
            for i in range(len(stack)):
                node = stack.pop(0)
                temp += [node._item]
                if node._left:  stack += [node._left]
                if node._right: stack += [node._right]
            res += [temp[::flag]]
            temp = []
            flag *= -1
        return res

bst = AdvBST3()
numbers = [3, 2, 20, 15, 27]
for i in numbers:
    bst.add(i)
bst.zigzagLevelOrder()