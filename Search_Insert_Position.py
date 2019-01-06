class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = int((start + end) / 2)
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        elif nums[start] > target:
            if start > 0:
                return start-1
            else:
                return start
        elif nums[end] < target:
            return end+1
        else:
            return start+1


if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 5
    finder = Solution()
    res = finder.searchInsert(nums, target)
    print(res)

