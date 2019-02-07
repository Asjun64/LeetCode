# 树
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



# 根据数组生成二叉树，空节点用 None
def createTree(treeList):
    """
    递归
    :type treeList: List
    :rtype TreeNode
    """
    if len(treeList) < 1 or treeList[0] == None:
        return None
    if len(treeList) == 1:
        return TreeNode(treeList[0])
    if treeList[0] == None:
        return None
    root = TreeNode(treeList[0])
    length = len(treeList)
    list_left = []
    list_right = []

    array = [1]
    while array:
        i = array.pop(0)
        # print(i, treeList, list_left, len(treeList), array)
        # print
        list_left.append(treeList[i])
        if 2*i+1 < length:
            array.append(2*i+1)
        if 2*i+2 < length:
            array.append(2*i+2)
    if length > 2:
        array = [2]
        while array:
            i = array.pop(0)
            # print(i, treeList, list_right, len(treeList), array)
            # print()
            list_right.append(treeList[i])
            if 2*i+1 < length:
                array.append(2*i+1)
            if 2*i+2 < length:
                array.append(2*i+2)
    root.left = createTree(list_left)
    root.right = createTree(list_right)
    return root


# 返回二叉树的最大高度，根节点高度为 1
def getTreeHigh(rootNode):
    """
    :type rootNode: TreeNode
    :rtype int
    """
    if rootNode == None:
        return 0
    array = [[rootNode,1]]
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


# 判断是否是叶节点
def isLeaf(node):
    return node and node.left == node.right == None

# 镜像翻转二叉树
def reversal(root):
    """
    :type root: TreeNode
    :rtype: None
    """
    if root == None or isLeaf(root):
        return
    node = root.left
    root.left = root.right
    root.right = node
    del node
    reversal(root.left)
    reversal(root.right)


# 辨别两个二叉树是否完全相等
def isEqual(tree1, tree2):
    """
    :type tree1, tree2: TreeNode
    :rtype bool
    """
    if tree1 == tree2 == None:
        return True
    elif tree1 == None or tree2 == None or tree1.val != tree2.val:
        return False
    elif isLeaf(tree1) and isLeaf(tree2):
        return True
    else:
        return isEqual(tree1.left, tree2.left) and isEqual(tree1.right, tree2.right)


# 辨别两个二叉树是否完全镜像
def isMirror(tree1, tree2):
    """
    :type tree1, tree2: TreeNode
    :rtype bool
    """
    if tree1 == tree2 == None:
        return True
    elif tree1 == None or tree2 == None or tree1.val != tree2.val:
        return False
    elif isLeaf(tree1) and isLeaf(tree2):
        return True
    else:
        return isMirror(tree1.left, tree2.right) and isMirror(tree1.right, tree2.left)


# 画出二叉树
def printTree(rootNode):
    """
    :type rootNode: TreeNode
    :rtype None
    """
    if rootNode == None:
        return
    treeHigh = getTreeHigh(rootNode)
    array = [[rootNode, 1]]
    print_high = 1
    nums = 2**(treeHigh-1)
    val_width = 4
    print("-"*nums*val_width)
    while array:
        item = array.pop(0)
        node = item[0]
        high = item[1]
        if high > print_high:
            print_high = high
            print()
            if print_high > treeHigh:
                break
        if node != None:
            print(str(node.val).center(nums*val_width//2**(high-1)), end="")
            array.append([None if node.left==None else node.left, high+1])
            array.append([None if node.right==None else node.right, high+1])
        else:
            print(" ".center(nums*val_width//2**(high-1)), end="")
            array.append([None, high+1])
            array.append([None, high+1])
    print("-"*nums*val_width)
    return
