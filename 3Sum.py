class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums, L = sorted(nums), len(nums)
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start, end = i+1, L-1
            while start < end:
                nums_sum = nums[start] + nums[end]
                if nums_sum == -nums[i]:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                elif nums_sum > -nums[i]:
                    end -= 1
                else:
                    start += 1
        return res


if __name__ == '__main__':
    array_nums = [-1, 0, 1, 2, -1, -4]
    finder = Solution()
    res = finder.threeSum(array_nums)
    print(res)
