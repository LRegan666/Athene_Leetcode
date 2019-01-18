class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = 0
        while n > 0:
            n = int(n / 5)
            r += n
        return r