class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        letters = ('A', 'B', 'C', 'D', 'E',
                   'F', 'G', 'H', 'I', 'J',
                   'K', 'L', 'M', 'N', 'O',
                   'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z')
        res = ''
        while n > 0:
            ind = (n - 1) % 26
            n = (n - 1) // 26
            if n == 0:
                return letters[ind] + res
            else:
                res = letters[ind] + res
        return res


if __name__ == '__main__':
    n = 27
    converter = Solution()
    res = converter.convertToTitle(n)
    print(res)

