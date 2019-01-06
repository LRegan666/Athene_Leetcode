import copy

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        new_nums = sorted(nums)
        res = []
        while True:
            res.append(new_nums)
            nums = copy.copy(new_nums)
            new_nums, status = self.next_permute(nums)
            if status == 0:
                break
        return res

    def next_permute(self, nums):
        ln, swap_index = len(nums), -1
        for i in range(ln-2, -1, -1):
            if nums[i] < nums[i+1]:
                swap_index = i
                break
        if swap_index == -1:
            return nums, 0
        for j in range(ln-1, -1, -1):
            if nums[swap_index] < nums[j]:
                nums[swap_index], nums[j] = nums[j], nums[swap_index]
                break
        self.quick_sort(nums, swap_index+1, ln-1)
        return nums, 1

    def quick_sort(self, nums, start, end):
        if start >= end:
            return
        pivot = nums[start]
        left, right = start+1, end
        while left <= right:
            while left <= right and nums[left] <= pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left > right:
                break
            nums[left], nums[right] = nums[right], nums[left]
        nums[start], nums[right] = nums[right], nums[start]
        self.quick_sort(nums, start, right-1)
        self.quick_sort(nums, right+1, end)

