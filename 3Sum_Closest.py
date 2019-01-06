class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums, L = sorted(nums), len(nums)
        difference, result = float('inf'), 0
        for i in range(L):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            residual = target - nums[i]
            start, end = i+1, L-1
            while start < end:
                cur_diff = residual - nums[start] - nums[end]
                if abs(cur_diff) < difference:
                    difference = abs(cur_diff)
                    result = nums[start] + nums[end] + nums[i]
                if cur_diff > 0:
                    start += 1
                else:
                    end -= 1
        return result


if __name__ == '__main__':
    nums = [-1,2,1,-4]
    target = 1
    counter = Solution()
    res = counter.threeSumClosest(nums, target)
    print(res)