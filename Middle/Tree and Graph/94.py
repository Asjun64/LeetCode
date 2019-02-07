# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal1(self, root):
        """
        递归
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root != None:
            res += self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)
        return res

    def inorderTraversal2(self, root):
        """
        迭代
        """
        res = []


def createTree(res):



arr = [1]
arr2 = [2,3 ,4]
arr += arr2

print(arr)