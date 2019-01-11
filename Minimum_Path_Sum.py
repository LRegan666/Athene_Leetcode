class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        for p in range(1, m):
            grid[p][0] = grid[p-1][0] + grid[p][0]
        for q in range(1, n):
            grid[0][q] = grid[0][q-1] + grid[0][q]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i-1][j]+grid[i][j], grid[i][j-1]+grid[i][j])
        return grid[-1][-1]


if __name__ == '__main__':
    grid = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    counter = Solution()
    res = counter.minPathSum(grid)
    print(res)

