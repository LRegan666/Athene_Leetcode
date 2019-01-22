class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n >= 10:
            n_str = str(n)
            new_sum = 0
            for s in n_str:
                new_sum += int(s) ** 2
            n = new_sum
        if n == 1 or n == 7:
            return True
        else:
            return False


if __name__ == '__main__':
    n = 15
    ret = Solution().isHappy(n)
    print(ret)
