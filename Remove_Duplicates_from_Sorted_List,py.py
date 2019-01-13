class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        phead = head
        prev_val = phead.val
        while phead.next:
            next_node = phead.next
            next_val = next_node.val
            if next_val == prev_val:
                phead.next = next_node.next
            else:
                prev_val = next_val
                phead = phead.next
        return head

