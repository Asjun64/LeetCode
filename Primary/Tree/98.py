# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import *

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 采用中序遍历
        # 遍历的值比前一个值小则返回 False
        if root == None:
            return True

        stack = [root]
        i = None
        flag = True
        while stack:
            node = stack[0]
            if node.left and flag:
                stack.insert(0, node.left)
            elif i == None or node.val > i:
                stack.pop(0)
                i = node.val
                flag = False
                if node.right:
                    stack.insert(0, node.right)
                    flag = True
            else:
                return False
        return True


def run():
    s = Solution()
    tree1 = createTree([5, 1, 4, None, None, 3, 6])

    print(s.isValidBST(tree1))

run()
