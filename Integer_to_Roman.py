class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        convert_dict = {0: ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
                        1: ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
                        2: ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
                        3: ['', 'M']}
        num = str(num)
        convert_res = []
        for i in range(len(num)-1, -1, -1):
            j = len(num) - i - 1
            if i == 3:
                tmp = convert_dict[i][1] * int(num[j])
                convert_res.append(tmp)
            else:
                tmp = convert_dict[i][int(num[j])]
                convert_res.append(tmp)
        return ''.join(convert_res)


if __name__ == '__main__':
    n = 1994
    converter = Solution()
    res = converter.intToRoman(n)
    print(res)