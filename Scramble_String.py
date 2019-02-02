class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not s1:
            return False
        if len(s1) == 1:
            status = True if s1 == s2 else False
            return status
        if sorted(s1) != sorted(s2):
            return False
        for i in range(len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
                    (self.isScramble(s1[i:], s2[:-i]) and self.isScramble(s1[:i], s2[-i:])):
                return True
        return False


if __name__ == '__main__':
    s1 = "abb"
    s2 = "bba"
    res = Solution().isScramble(s1, s2)
    print(res)
