class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums:
            start, end = 0, len(nums)-1
            self.quick_sort(nums, start, end)

    def quick_sort(self, nums, start, end):
        if start >= end:
            return
        pivot = nums[start]
        left, right = start+1, end
        while left <= right:
            while left <= right and nums[left] <= pivot:
                left += 1
            while left <= right and nums[right] >= pivot:
                right -= 1
            if left > right:
                break
            nums[left], nums[right] = nums[right], nums[left]
        nums[start], nums[right] = nums[right], nums[start]
        self.quick_sort(nums, start, right-1)
        self.quick_sort(nums, right+1, end)

if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    arrange = Solution()
    arrange.sortColors(nums)
    print(nums)
