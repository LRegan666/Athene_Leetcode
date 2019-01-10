# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if k == 0:
            return head
        phead, tail = head, None
        l = 0
        while phead:
            l += 1
            if not phead.next:
                tail = phead
            phead = phead.next
        steps = k % l
        i = 0
        phead = head
        while i < l-steps-1:
            phead = phead.next
            i += 1
        old_head = head
        new_head = phead.next
        phead.next = None
        tail.next = old_head
        return new_head

