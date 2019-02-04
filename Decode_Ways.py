class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp = [0] * len(s)
        dp[0] = 1
        if 1 <= int(s[:2]) <= 26:
            if s[1] != '0':
                dp[1] = 2
            else:
                dp[1] = 1
        elif s[1] != '0':
            dp[1] = 1
        else:
            pass
        for i in range(2, len(s)):
            if s[i-1] != '0' and 1 <= int(s[i-1:i+1]) <= 26:
                if s[i] != '0':
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-2]
            elif s[i] != '0':
                dp[i] = dp[i-1]
            else:
                break
        return dp[-1]


if __name__ == '__main__':
    s = '101'
    res = Solution().numDecodings(s)
    print(res)
