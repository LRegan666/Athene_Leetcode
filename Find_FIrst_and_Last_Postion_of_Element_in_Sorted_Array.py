class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        start, end = 0, len(nums)-1
        if nums[start] == target and nums[end] == target:
            return [start, end]
        while start+1 < end:
            mid = int((start + end) / 2)
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] == target and nums[end] == target:
            while start > 0 and nums[start-1] == target:
                start -= 1
            while end < len(nums)-1 and nums[end+1] == target:
                end += 1
            return [start, end]
        elif nums[start] == target:
            end = start
            while start > 0 and nums[start-1] == target:
                start -= 1
            return [start, end]
        elif nums[end] == target:
            start = end
            while end < len(nums)-1 and nums[end+1] == target:
                end += 1
            return [start, end]
        else:
            return [-1, -1]


if __name__ == '__main__':
    nums = [2, 2]
    target = 2
    finder = Solution()
    res = finder.searchRange(nums, target)
    print(res)

