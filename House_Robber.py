class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        L = len(nums)
        dp = [0]*L
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, L):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]


if __name__ == '__main__':
    nums = [2, 1, 1, 2]
    finder = Solution()
    res = finder.rob(nums)
    print(res)

