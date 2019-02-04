class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        S = [0]*(n+1)
        T = [[0 for _ in range(n+1)] for _ in range(n+1)]
        S[0], S[1] = 1, 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                T[j][i] = S[j-1] * S[i-j]
                if i != 1:
                    S[i] += T[j][i]
        return S[-1]

if __name__ == '__main__':
    n = 3
    res = Solution().numTrees(n)
    print(res)
