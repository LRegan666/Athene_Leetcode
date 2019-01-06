class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        ln = len(nums)
        swap_index = -1
        for i in range(ln-2, -1, -1):
            if nums[i] < nums[i+1]:
                swap_index = i
                break
        if swap_index == -1:
            nums.sort()
            return nums
        for j in range(ln-1, swap_index, -1):
            if nums[j] > nums[swap_index]:
                nums[j], nums[swap_index] = nums[swap_index], nums[j]
                break
        self.quick_sort(nums, swap_index+1, ln-1)

    def quick_sort(self, array, lower, upper):
        if lower > upper:
            return
        pivot = array[lower]
        left, right = lower+1, upper
        while left <= right:
            while left <= right and array[left] < pivot:
                left += 1
            while left <= right and array[right] >= pivot:
                right -= 1
            if left > right:
                break
            array[left], array[right] = array[right], array[left]
        array[right], array[lower] = array[lower], array[right]
        self.quick_sort(array, lower, right-1)
        self.quick_sort(array, right+1, upper)


if __name__ == '__main__':
    nums = [3,2,1]
    generator = Solution()
    generator.nextPermutation(nums)
    print(nums)
