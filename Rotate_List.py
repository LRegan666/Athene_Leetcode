class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        phead, tail = head, None
        l = 0
        while phead:
            l += 1
            if not phead.next:
                tail = phead
            phead = phead.next
        steps = k % l
        if steps == 0:
            return head
        phead = ListNode(0)
        phead.next = head
        i = 0
        while i < l-steps:
            phead = phead.next
            i += 1
        old_head = head
        new_head = phead.next
        phead.next = None
        tail.next = old_head
        return new_head

