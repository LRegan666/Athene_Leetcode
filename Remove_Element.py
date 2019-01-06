class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        i = 0
        status = False
        while i < len(nums):
            while i <= len(nums)-1 and nums[i] == val:
                nums.pop(i)
                status = True
            if status:
                break
            else:
                i += 1
        return len(nums)


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    finder = Solution()
    print(finder.removeElement(nums, val))