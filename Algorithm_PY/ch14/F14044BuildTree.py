# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 1:44 PM 5/8/20

Question: 

"""
from BinarySearchTree import BinarySearchTree
from BinarySearchTree import Node
def buildTree(preorder, inorder):
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = Node(inorder[ind])
        root._left = buildTree(preorder, inorder[0:ind])
        root._right = buildTree(preorder, inorder[ind+1:])
        return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = buildTree(preorder, inorder)