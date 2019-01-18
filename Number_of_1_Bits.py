class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits, count = 31, 0
        while bits > -1:
            if n & 1 << bits:
                count += 1
            bits -= 1
        return count


if __name__ == '__main__':
    n = 0b11111111111111111111111111111101
    counter = Solution()
    res = counter.hammingWeight(n)
    print(res)

