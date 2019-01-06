class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        map_dict = {'2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz'}
        res = [letter for letter in map_dict[digits[0]]]
        for digit in digits[1:]:
            for item in res:
                res = res + [item+letter for letter in map_dict[digit]]
                res.remove(item)
        return res


if __name__ == '__main__':
    n = "23"
    converter = Solution()
    s = converter.letterCombinations(n)
    print(s)
