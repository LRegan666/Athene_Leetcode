class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            item = nums[i]
            j = i + 1
            while j < len(nums) and nums[j] == item:
                nums.pop(j)
            i += 1
        return len(nums), nums


if __name__ == '__main__':
    nums = [1, 1, 2]
    filter = Solution()
    print(filter.removeDuplicates(nums))