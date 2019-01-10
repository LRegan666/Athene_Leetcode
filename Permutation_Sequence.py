class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return "1"
        nums = list(range(1, n+1))
        i = 1
        while i < k:
            self.permutation_sequence(nums, n)
            i += 1
        return ''.join([str(num) for num in nums])

    def permutation_sequence(self, nums, n):
        swap_index = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                swap_index = i
                break
        if swap_index == -1:
            return
        for j in range(n-1, -1, -1):
            if nums[j] > nums[swap_index]:
                nums[j], nums[swap_index] = nums[swap_index], nums[j]
                break
        self.quick_sort(nums, swap_index+1, n-1)

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
        nums[right], nums[start] = nums[start], nums[right]
        self.quick_sort(nums, start, right-1)
        self.quick_sort(nums, right+1, end)


if __name__ == '__main__':
    n, k = 4, 9
    finder = Solution()
    res = finder.getPermutation(n, k)
    print(res)
