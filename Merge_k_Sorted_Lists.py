class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        values = []
        dummy_node = ListNode(0)
        head = dummy_node
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next
        values.sort()
        for value in values:
            new_node = ListNode(value)
            head.next = new_node
            head = head.next
        return dummy_node.next

