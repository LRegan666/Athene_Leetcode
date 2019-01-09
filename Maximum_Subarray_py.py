class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = self.divide_and_conquer(nums)
        return max(res)

    def divide_and_conquer(self, nums):
        if len(nums) == 1:
            return nums[0], nums[0], nums[0], nums[0]
        mid = int(len(nums) / 2)
        left = self.divide_and_conquer(nums[:mid])
        right = self.divide_and_conquer(nums[mid:])
        l = max((left[0], left[3], left[3]+right[0]))
        m = max((left[1], left[2]+right[0], right[1]))
        r = max((right[2], right[3], right[3]+left[2]))
        a = left[3]+right[3]
        return l, m, r, a


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    finder = Solution()
    res = finder.maxSubArray(nums)
    print(res)

