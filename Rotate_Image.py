import numpy as np

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        for k in range(n):
            for p in range(int(n/2)):
                matrix[k][p], matrix[k][n-1-p] = matrix[k][n-1-p], matrix[k][p]


if __name__ == '__main__':
    m = [
        [ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
    ]
    converter = Solution()
    converter.rotate(m)
    print(np.mat(m))
