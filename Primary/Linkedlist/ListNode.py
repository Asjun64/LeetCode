# 单向链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_List(my_list):
    """
    :type my_list: list
    :rtype: ListNode
    """
    dummy = ListNode(0)
    head = dummy
    for i in my_list:
        dummy.next = ListNode(i)
        dummy = dummy.next
    return head.next

def print_list(my_list):
    """
    :type my_list: ListNode
    """
    while my_list:
        print(my_list.val)
        my_list = my_list.next
