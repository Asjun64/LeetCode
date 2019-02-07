# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        fa = dummy
        this_node = head
        son = this_node.next
        while son:
            this_node.next = fa
            fa = this_node
            this_node = son
            son = son.next
        this_node.next = fa
        head.next = None
        return this_node
