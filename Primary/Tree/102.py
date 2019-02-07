# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import *

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        array = [[root, 1]]
        result = []
        item = []
        now_high = 1
        while array:
            p = array.pop(0)
            node = p[0]
            high = p[1]
            if high > now_high:
                now_high = high
                result.append(item)
                item = []
            item.append(node.val)
            if node.left:
                array.append([node.left, high+1])
            if node.right:
                array.append([node.right, high+1])
        result.append(item)
        return result


s = Solution()
l1 = [3, 9, 20, None, None, 15, 7]
tree1 = createTree(l1)

printTree(tree1)
print(s.levelOrder(tree1))
