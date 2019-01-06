class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        i, n_jump = 0, 0
        l = len(nums)
        current_region, next_region = 0, 0
        while True:
            while i <= next_region:
                current_region = max(i+nums[i], current_region)
                if current_region >= l-1:
                    return n_jump+1
                i += 1
            next_region = current_region
            n_jump += 1


if __name__ == '__main__':
    nums = [2,3,1,1,4]
    counter = Solution()
    res = counter.jump(nums)
    print(res)

