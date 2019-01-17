class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = ('A', 'B', 'C', 'D', 'E',
                   'F', 'G', 'H', 'I', 'J',
                   'K', 'L', 'M', 'N', 'O',
                   'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z')
        map_dict = dict(zip(letters, tuple(range(1, 27))))
        ls = len(s)
        res = 0
        for i in range(ls):
            res += map_dict[s[i]] * 26 ** (ls - 1 - i)
        return res


if __name__ == '__main__':
    s = "A"
    converter = Solution()
    res = converter.titleToNumber(s)
    print(res)

