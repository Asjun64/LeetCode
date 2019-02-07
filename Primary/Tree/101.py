# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, tree1, tree2):
        if tree1 == tree2 == None:
            return True
        elif tree1 == None or tree2 == None or tree1.val != tree2.val:
            return False
        elif self.isLeaf(tree1) and self.isLeaf(tree2):
            return True
        else:
            return self.isMirror(tree1.left, tree2.right) and self.isMirror(tree1.right, tree2.left)

    def isLeaf(self, root):
        return root and root.left == root.right == None
