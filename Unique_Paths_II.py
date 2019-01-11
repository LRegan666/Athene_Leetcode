class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for p in range(n)] for _ in range(m)]
        for p in range(m):
            if obstacleGrid[p][0] == 0:
                dp[p][0] = 1
            else:
                break
        for q in range(n):
            if obstacleGrid[0][q] == 0:
                dp[0][q] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    grid = [
        [0,1],
        [0,0]
    ]
    counter = Solution()
    res = counter.uniquePathsWithObstacles(grid)
    print(res)

