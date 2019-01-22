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

    def mergeList(self, node, mid):
        


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
