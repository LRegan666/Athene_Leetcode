class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s:
            if not p or p == '*':
                return True
            else:
                return False
        ls, lp = len(s), len(p)
        dp = [[False for _ in range(lp+1)] for _ in range(ls+1)]
        dp[-1][-1] = True
        for i in range(ls, -1, -1):
            for j in range(lp-1, -1, -1):
                current_match = i < ls and p[j] in (s[i], '?', '*')
                if i < ls and p[j] == '*':
                    dp[i][j] = current_match and (dp[i][j+1] or dp[i+1][j] or dp[i+1][j+1])
                elif i == ls and p[j] == '*':
                    dp[i][j] = dp[i][j+1]
                else:
                    dp[i][j] = current_match and dp[i+1][j+1]
        return dp[0][0]


if __name__ == '__main__':
    s = "a"
    p = "a*"
    matcher = Solution()
    res = matcher.isMatch(s, p)
    print(res)
