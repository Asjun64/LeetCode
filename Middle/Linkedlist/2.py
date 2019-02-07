class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        res.val = 0
        res.next = ListNode(0)
        header = res

        c = 0
        while (l1 and l2):
            res = res.next

            res.val = l1.val + l2.val + c

            c = res.val // 10
            res.val %= 10

            l1 = l1.next
            l2 = l2.next
            res.next = ListNode(0)

        while l1 :
            res = res.next
            res.val = l1.val + c

            c = res.val // 10
            res.val %= 10

            l1 = l1.next
            res.next = ListNode(0)
        while l2 :
            res = res.next
            res.val = l2.val + c

            c = res.val // 10
            res.val %= 10

            l2 = l2.next
            res.next = ListNode(0)
        if (c > 0):
            res = res.next
            res.val = c
        else:
            res.next = None
        return header.next

def listNode2Num(listNode):
    arr = []
    while listNode:
        arr.append(listNode.val)
        listNode = listNode.next
    arr = arr[::-1]
    res = 0
    for i in arr:
        res *= 10
        res += i
    return res

def printListNode(listNode) :
    arr = []
    while listNode:
        arr.append(listNode.val)
        listNode = listNode.next
    arr = arr[::-1]
    print(arr)


def createListNode(num):
    res = ListNode(0)
    res.next = ListNode(0)
    head = res
    if num == 0 :
        return head.next
    while num:
        res = res.next
        res.val = num % 10
        num //= 10
        res.next = ListNode(0)
    res.next = None
    return head.next

def autoTest(n1, n2):
    l1 = createListNode(n1)
    l2 = createListNode(n2)
    l3 = Solution().addTwoNumbers(l1, l2)

    n3 = listNode2Num(l3)

    print(str(n1) + " + " + str(n2) + " = " + str(n3))

    printListNode(l3)


arrs = [
    # [111, 222],
    # [0, 0],
    # [3, 2],
    # [222, 444],
    # [24, 234],
    [99, 9999],
]

for arr in arrs:
    autoTest(arr[0], arr[1])

# autoTest(111, 222)