class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        lh, ln = len(haystack), len(needle)
        for i in range(lh-ln+1):
            if haystack[i:i+ln] == needle:
                return i
        return -1


if __name__ == '__main__':
    haystack = "aaaaa"
    needle = "bba"
    finder = Solution()
    print(finder.strStr(haystack, needle))