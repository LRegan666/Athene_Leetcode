class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) == 4 and sum(nums) == target:
            return [nums]
        nums, L = sorted(nums), len(nums)
        res = []
        for i in range(L):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, L):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                residual = target - nums[i] - nums[j]
                start, end = j+1, L-1
                while start < end:
                    tmp = nums[start] + nums[end]
                    if tmp == residual:
                        res.append([nums[i], nums[j], nums[start], nums[end]])
                        start += 1
                        while start < end and nums[start] == nums[start-1]:
                            start += 1
                    elif tmp > residual:
                        end -= 1
                    else:
                        start += 1
        return res


if __name__ == '__main__':
    nums = [-3,-2,-1,0,0,1,2,3]
    target = 0
    finder = Solution()
    res = finder.fourSum(nums, target)
    print(res)