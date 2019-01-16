class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pheadA, pheadB = headA, headB
        lA, lB = 0, 0
        while pheadA:
            lA += 1
            pheadA = pheadA.next
        while pheadB:
            lB += 1
            pheadB = pheadB.next
        gap = abs(lA - lB)
        i = 0
        pA, pB = headA, headB
        if lA > lB:
            while i < gap:
                pA = pA.next
                i += 1
        else:
            while i < gap:
                pB = pB.next
                i += 1
        while pA != pB:
            pA = pA.next
            pB = pB.next
        if pA:
            return pA
        else:
            return None

