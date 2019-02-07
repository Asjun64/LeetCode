# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        node_1 = node_2 = dummy
        for i in range(n+1):
            node_1 = node_1.next

        while node_1 != None:
            node_1 = node_1.next
            node_2 = node_2.next

        node_1 = node_2.next
        node_2.next = node_1.next
        node_2 = dummy.next
        del node_1, dummy
        return node_2
