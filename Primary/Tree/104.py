# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        array = [[root,1]]
        max_deep = 0
        while array:
            node = array.pop(0)
            p = node[0]
            deep = node[1]
            if deep > max_deep:
                max_deep = deep

            if p.left:
                array.append([p.left, deep+1])
            if p.right:
                array.append([p.right, deep+1])
        return max_deep
