# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        fast_p = head.next
        slow_p = head
        while fast_p:
            if fast_p == slow_p:
                return True
            fast_p = fast_p.next
            if fast_p:
                fast_p = fast_p.next
            else:
                return False
            slow_p = slow_p.next
        return False
