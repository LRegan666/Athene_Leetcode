import math

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        i, circles = 0, math.ceil(m/2.0)
        records = {'r': [], 'c': []}
        while i < m:
            for r in range(i, m):
                if i >= n:
                    break
                if matrix[r][i] == 0:
                    if r not in records['r']:
                        records['r'].append(r)
                    if i not in records['c']:
                        records['c'].append(i)
            for c in range(i, n):
                if matrix[i][c] == 0:
                    if c not in records['c']:
                        records['c'].append(c)
                    if i not in records['r']:
                        records['r'].append(i)
            i += 1
        for r in records['r']:
            for j in range(n):
                matrix[r][j] = 0
        for c in records['c']:
            for k in range(m):
                matrix[k][c] = 0


if __name__ == '__main__':
    matrix = [
        [1, 0, 3]
    ]
    converter = Solution()
    converter.setZeroes(matrix)
    print(matrix)

