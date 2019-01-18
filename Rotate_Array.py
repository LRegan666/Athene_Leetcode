class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums:
            for _ in range(k):
                cur_val = nums.pop()
                nums.insert(0, cur_val)