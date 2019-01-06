class Solution:
    def isMatch(self, s, p):
        """
        '.' 匹配任意单字符
        '*' 匹配0或多个前一个字符
        """
        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                first_match = i < len(s) and p[j] in (s[i], '.')
                if j < len(p)-1 and p[j+1] == '*':
                    dp[i][j] = (first_match and dp[i+1][j]) or dp[i][j+2]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]

    def isMatch_Recursion(self, s, p):
        if not p:
            return not s
        first_match = bool(s) and p[0] in (s[0], '.')
        if len(p) >= 2 and p[1] == '*':
            return (first_match and self.isMatch_Recursion(s[1:], p)) \
                   or self.isMatch_Recursion(s, p[2:])
        else:
            return first_match and self.isMatch_Recursion(s[1:], p[1:])

    def isMatch_DP(self, s, p):
        mem = {}
        def dp(i, j):
            if (i, j) in mem:
                return mem[i, j]
            if j == len(p):
                ans = (i == len(s))
            else:
                first_match = bool(s[i:]) and p[j] in (s[i], '.')
                if j < len(p)-1 and p[j+1] == '*':
                    ans = (first_match and dp(i+1, j)) or dp(i, j+2)
                else:
                    ans = first_match and dp(i+1, j+1)
            mem[i, j] = ans
            return ans
        return dp(0, 0)


if __name__ == '__main__':
    s, p = 'mississippi', 'mis*is*p*.'
    matcher = Solution()
    res = matcher.isMatch(s, p)
    print(res)
