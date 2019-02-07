# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from ListNode import *

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        p = head

        new_list = []
        while p:
            new_list.append(p.val)
            p = p.next
        i = 0
        j = len(new_list)-1
        while i<j:
            if new_list[i] != new_list[j]:
                return False
            i = i+1
            j = j-1
        return True
