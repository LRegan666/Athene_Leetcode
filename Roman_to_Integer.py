class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        convert_dict = {0: ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
                        1: ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
                        2: ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']}
        i, res = 0, 0
        if i == 0 and s[i] == 'M':
            while i < len(s) and s[i] == 'M':
                i += 1
            res += 1000*i
        for j in range(2, -1, -1):
            for k in range(4, 0, -1):
                if s[i:i+k] in convert_dict[j]:
                    res += convert_dict[j].index(s[i:i+k]) * 10**j
                    i += k
                    break
        return res


if __name__ == '__main__':
    s = 'MMM'
    converter = Solution()
    res = converter.romanToInt(s)
    print(res)