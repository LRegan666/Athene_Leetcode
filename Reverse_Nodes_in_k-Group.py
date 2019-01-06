class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy_node = ListNode(0)
        dummy_node.next = head
        current_node = dummy_node
        exec_status = True
        while current_node:
            check_node = current_node
            i = 0
            while exec_status and i < k:
                if not check_node.next:
                    exec_status = False
                    break
                check_node = check_node.next
                i += 1
            if exec_status:
                tmp_node1 = current_node.next
                tmp_node2 = check_node.next
                current_node.next = check_node
                current_node = current_node.next
                j = k - 2
                while j > 0:
                    adjust_node = tmp_node1
                    for _ in range(j):
                        adjust_node = adjust_node.next
                    current_node.next = adjust_node
                    current_node = current_node.next
                    j -= 1
                current_node.next = tmp_node1
                current_node = current_node.next
                current_node.next = tmp_node2
            else:
                break
        return dummy_node.next
