class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        sorted_node = ListNode(head.val)
        pnode = sorted_node
        current_length = 0
        while head:
            if head.val >= pnode.val:
                pnode.next = head
                pnode = pnode.next
                current_length += 1
                head = head.next
            else:
                add_head = head
                head = head.next
                mid = int(current_length / 2)
                mid_node = sorted_node
                pre_mid_node = sorted_node
                for _ in range(mid):
                    pre_mid_node = mid_node
                    mid_node = mid_node.next
                self.insert_node(sorted_node, pre_mid_node, mid_node, mid, current_length, add_head)
                current_length += 1
        pnode.next = None
        return sorted_node.next

    def insert_node(self, left_node, pre_mid_node, mid_node, mid, total, add_node):
        if mid == 0 or mid_node.val == add_node.val:
            if pre_mid_node == left_node and mid_node == left_node:
                mid_node = mid_node.next
            pre_mid_node.next = add_node
            pre_mid_node = pre_mid_node.next
            pre_mid_node.next = mid_node
            return
        if mid_node.val > add_node.val:
            current_total = mid
            current_mid = int((current_total - 1) / 2)
            current_mid_node = left_node
            current_pre_mid_node = left_node
            for _ in range(current_mid):
                current_pre_mid_node = current_mid_node
                current_mid_node = current_mid_node.next
            self.insert_node(left_node, current_pre_mid_node, current_mid_node, current_mid, current_total, add_node)
        elif mid_node.next and mid_node.val < add_node.val <= mid_node.next.val:
            tmp = mid_node.next
            mid_node.next = add_node
            mid_node = mid_node.next
            mid_node.next = tmp
        else:
            current_total = total - mid
            current_mid = int((current_total - 1) / 2)
            left_node = mid_node.next
            current_mid_node = left_node
            current_pre_mid_node = mid_node
            for _ in range(current_mid):
                current_pre_mid_node = current_mid_node
                current_mid_node = current_mid_node.next
            self.insert_node(left_node, current_pre_mid_node, current_mid_node, current_mid, current_total, add_node)


if __name__ == '__main__':
    node_values = [-84, 142, 41, -17, -71, 170, 186, 183, -21, -76, 76, 10, 29, 81, 112, -39, -6, -43, 58, 41, 111, 33, 69, 97, -38,
     82, -44, -7, 99, 135, 42, 150, 149, -21, -30, 164, 153, 92, 180, -61, 99, -81, 147, 109, 34, 98, 14, 178, 105, 5,
     43, 46, 40, -37, 23, 16, 123, -53, 34, 192, -73, 94, 39, 96, 115, 88, -31, -96, 106, 131, 64, 189]
    for v in (5, -3, 1, 8, 5, 11, 15):
        head = ListNode(4)
        phead = head
        for val in node_values:
            curnode = ListNode(val)
            phead.next = curnode
            phead = phead.next
        phead.next = None
        sorter = Solution()
        node = sorter.sortList(head)
        res = []
        while node:
            res.append(node.val)
            node = node.next
        print(res)
        break
