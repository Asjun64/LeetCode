# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from ListNode import *

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        head = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        while l1:
            dummy.next = l1
            dummy = dummy.next
            l1 = l1.next
        while l2:
            dummy.next = l2
            dummy = dummy.next
            l2 = l2.next
        return head.next


def run():
    l1 = create_List([1, 2, 4])
    l2 = create_List([1, 3, 4])

    s = Solution()

    l3 = s.mergeTwoLists(l1, l2)
    print_list(l3)


run()
