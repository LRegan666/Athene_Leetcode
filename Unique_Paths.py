class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 if p == 0 else 0 for p in range(n)] for _ in range(m)]
        for k in range(1, n):
            dp[0][k] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


if __name__ == '__main__':
    m, n = 3, 2
    counter = Solution()
    res = counter.uniquePaths(m, n)
    print(res)

