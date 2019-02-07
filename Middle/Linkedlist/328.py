
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        node = head
        l2 = ListNode(0)
        tmp = l2
        while node:
            tmp.next = node.next
            tmp = tmp.next
            if tmp and tmp.next:
                node.next = tmp.next
            else:
                break
            node = node.next
        node.next = l2.next
        return head

def list2arr(listNode):
    arr = []
    while listNode:
        arr.append(listNode.val)
        listNode = listNode.next
    return arr

def createListNode(arr):
    head = ListNode(0)
    tmp = head
    for i in arr:
        tmp.next = ListNode(0)
        tmp = tmp.next
        tmp.val = i
    return head.next


s = Solution()

l1 = createListNode([])

l2 = s.oddEvenList(l1)

arr2 = list2arr(l2)
print(arr2)