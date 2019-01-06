class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pNode = head
        l = 0
        while pNode:
            l += 1
            pNode = pNode.next
        curNode = head
        positions = l - n
        while positions > 1:
            curNode = curNode.next
            positions -= 1
        if positions == 0:
            head = head.next
        else:
           curNode.next = curNode.next.next
        return head