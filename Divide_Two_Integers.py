class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        dend, sor = abs(dividend), abs(divisor)
        res = 0
        if sor == 1:
            res = dend
        else:
            factor, n_factor = sor, 1
            while dend >= sor:
                dend -= factor
                res += n_factor
                factor += factor
                n_factor += n_factor
                if factor > dend:
                    factor = sor
                    n_factor = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            return -res
        else:
            if res == 2147483648:
                res -= 1
            return res


if __name__ == '__main__':
    dividend, divisor = 10, 3
    counter = Solution()
    print(counter.divide(dividend, divisor))

