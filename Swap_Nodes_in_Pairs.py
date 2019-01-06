class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy_node = ListNode(0)
        dummy_node.next = head
        current_node = dummy_node
        while current_node:
            if current_node.next and current_node.next.next:
                tmp_node1 = current_node.next
                current_node.next = current_node.next.next
                current_node = current_node.next
                tmp_node2 = current_node.next
                current_node.next = tmp_node1
                current_node = current_node.next
                current_node.next = tmp_node2
            else:
                current_node = current_node.next
        return dummy_node.next