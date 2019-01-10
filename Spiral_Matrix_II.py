import math

import numpy as np

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        i, c = 0, math.ceil(n/2.0)
        num = 1
        while i < c:
            for j in range(i, n-i):
                matrix[i][j] = num
                num += 1
            j = n-i-1
            for k in range(i+1, n-i):
                matrix[k][j] = num
                num += 1
            if 2*i+1 < n:
                for m in range(j-1, i-1, -1):
                    matrix[j][m] = num
                    num += 1
            if j > i:
                for p in range(j-1, i, -1):
                    matrix[p][i] = num
                    num += 1
            i += 1
        return matrix


if __name__ == '__main__':
    n = 4
    generator = Solution()
    m = generator.generateMatrix(n)
    print(np.mat(m))

