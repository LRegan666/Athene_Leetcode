class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        ls = len(s)
        res, position = 0, 0
        for i in range(ls-1, -1, -1):
            if s[i] != ' ':
                position = i
                break
        for j in range(position, -1, -1):
            if s[j] == ' ':
                break
            res += 1
        return res


if __name__ == '__main__':
    s = "Hello World"
    counter = Solution()
    res = counter.lengthOfLastWord(s)
    print(res)

