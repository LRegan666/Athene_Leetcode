class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        if not s:
            return res
        stack = []
        for i in range(len(s)):
            if stack and s[i] == ')' and stack[-1][1] == '(':
                stack.pop()
                if stack:
                    current_length = i - stack[-1][0]
                else:
                    current_length = i + 1
                if current_length > res:
                    res = current_length
            else:
                stack.append((i, s[i]))
        return res

    def longestValidParentheses_DP(self, s):
        if not s:
            return 0
        m = len(s)
        dp = [0]*m
        for i in range(1, m):
            if s[i] == ')':
                if s[i-1] == '(':
                    if i >= 2:
                        dp[i] = dp[i-2] + 2
                    else:
                        dp[i] = 2
                else:
                    if i - dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                        ind = i - dp[i-1] - 2
                        if ind > 0:
                            dp[i] = dp[i-1] + dp[ind] + 2
                        else:
                            dp[i] = dp[i-1] + 2
        return max(dp)


if __name__ == '__main__':
    s = "(())))"
    checker = Solution()
    res = checker.longestValidParentheses_DP(s)
    print(res)
