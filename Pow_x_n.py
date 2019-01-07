class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        un = abs(n)
        i, factor = 1, x
        j, res = 1, 1
        while j <= un:
            res *= factor
            factor *= factor
            i += i
            if j+i > un:
                factor = x
                i = 1
            j += i
        if n < 0:
            return 1/res
        else:
            return res


if __name__ == '__main__':
    x, n = 2.00000, -2
    computer = Solution()
    res = computer.myPow(x, n)
    print(res)
