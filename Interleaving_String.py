class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [False] * (len(s2)+1)
        for i in range(-1, len(s1)):
            if i == -1:
                for j in range(-1, len(s2)):
                    if j == -1:
                        dp[j+1] = True
                    else:
                        dp[j+1] = (s2[j] == s3[i+j+1])
            else:
                for k in range(-1, len(s2)):
                    if k == -1:
                        dp[k+1] = (s1[i] == s3[i+k+1] and dp[k+1])
                    else:
                        dp[k+1] = (s1[i] == s3[i+k+1] and dp[k+1]) or (s2[k] == s3[i+k+1] and dp[k])
        return dp[-1]


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    res = Solution().isInterleave(s1, s2, s3)
    print(res)
