# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        small_node, large_node = ListNode(0), ListNode(0)
        psmall_node, plarge_node = small_node, large_node
        while head:
            if head.val < x:
                psmall_node.next = head
                psmall_node = psmall_node.next
            else:
                plarge_node.next = head
                plarge_node = plarge_node.next
            head = head.next
        plarge_node.next = None
        psmall_node.next = large_node.next
        return small_node.next
