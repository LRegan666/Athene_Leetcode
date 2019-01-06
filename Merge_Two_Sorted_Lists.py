class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        compore the value of current node for the combined linked list
        """
        dummy_node = ListNode(0)
        head = dummy_node
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        while l1:
            head.next = l1
            head = head.next
            l1 = l1.next
        while l2:
            head.next = l2
            head = head.next
            l2 = l2.next
        return dummy_node.next