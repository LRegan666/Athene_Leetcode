class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        dumb_node = ListNode(0)
        dumb_node.next = head
        phead = dumb_node
        i = 0
        while phead:
            if i+1 == m:
                pre_node = phead.next
                cur_node = phead.next.next
                i += 2
                while i <= n:
                    next_node = cur_node.next
                    cur_node.next = pre_node
                    pre_node = cur_node
                    cur_node = next_node
                    i += 1
                next_phead = phead.next
                phead.next.next = cur_node
                phead.next = pre_node
                phead = next_phead
            else:
                phead = phead.next
            i += 1
        return head
