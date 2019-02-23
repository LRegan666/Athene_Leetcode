class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = list(range(len(word2)+1))
        prev = 0
        for i in range(1, len(word1)+1):
            for j in range(len(dp)):
                if j == 0:
                    prev = dp[j]
                    dp[j] = i
                else:
                    if word2[j-1] == word1[i-1]:
                        tmp = dp[j]
                        dp[j] = prev
                        prev = tmp
                    else:
                        tmp = dp[j]
                        dp[j] = 1 + min(dp[j], dp[j-1], prev)
                        prev = tmp
        return dp[-1]


    def minDistance_recursion(self, word1, word2):
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word1)
        if not word2:
            return len(word2)
        if word1[0] == word2[0]:
            return self.minDistance_recursion(word1[1:], word2[1:])
        d = 1 + self.minDistance_recursion(word1[1:], word2)
        r = 1 + self.minDistance_recursion(word1[1:], word2[1:])
        i = 1 + self.minDistance_recursion(word1, word2[1:])
        return min(d, r, i)

    def minDistance_memo(self, word1, word2):
        if not word1 or not word2:
            return max(len(word1), len(word2))
        memo = [[-1 for _ in range(len(word2))] for _ in range(len(word1))]
        res = self._minDistance_recursion(word1, word2, 0, 0, memo)
        return res

    def _minDistance_recursion(self, w1, w2, i, j, memo):
        if i == len(w1) and j == len(w2):
            return 0
        if i == len(w1):
            return len(w2) - j
        if j == len(w2):
            return len(w1) - i
        if memo[i][j] == -1:
            if w1[i] == w2[j]:
                ans = self._minDistance_recursion(w1, w2, i+1, j+1, memo)
            else:
                d = 1 + self._minDistance_recursion(w1, w2, i+1, j, memo)
                r = 1 + self._minDistance_recursion(w1, w2, i+1, j+1, memo)
                it = 1 + self._minDistance_recursion(w1, w2, i, j+1, memo)
                ans = min(d, r, it)
            memo[i][j] = ans
        return memo[i][j]


if __name__ == '__main__':
    word1, word2 = "horse", "ros"
    res = Solution().minDistance(word1, word2)
    print(res)
