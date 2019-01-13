import math

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        while i * i < x:
            i += 1
        if i * i == x:
            return i
        else:
            return i - 1

    # Newton Method
    def mysqrt_pe(self, x):
        acc = 1e-6
        x_n = x / 2.00000
        while abs(x_n * x_n - x) > acc:
            x_n = (x_n + x / x_n) / 2.000000
        return int(math.floor(x_n))


if __name__ == '__main__':
    x = 8
    computer = Solution()
    res = computer.mysqrt_pe(x)
    print(res)

