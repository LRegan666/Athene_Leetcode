import math

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        n, m = len(matrix), len(matrix[0])
        c = min(n/2.0, m/2.0)
        c = int(math.ceil(c))
        i = 0
        res = []
        while i < c:
            for j in range(i, m-i):
                res.append(matrix[i][j])
            j = m-i-1
            for k in range(i+1, n-i):
                res.append(matrix[k][j])
            if 2*i+1 < n:
                for p in range(j-1, i-1, -1):
                    res.append(matrix[n-i-1][p])
            if j > i:
                for q in range(n-i-2, i, -1):
                    res.append(matrix[q][i])
            i += 1
        return res


if __name__ == '__main__':
    matrix = [
        [7],
        [9],
        [6]
    ]
    sorter = Solution()
    res = sorter.spiralOrder(matrix)
    print(res)

