class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                count, j = 1, i + 1
                while j < len(nums) and nums[j] == nums[i]:
                    count += 1
                    if count > 2:
                        nums[j] = 'r'
                    j += 1
                i = j
            else:
                i += 1
        k = 0
        while k < len(nums):
            if nums[k] == 'r':
                del nums[k]
            else:
                k += 1
        return len(nums)


if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    filter = Solution()
    res = filter.removeDuplicates(nums)
    print(res)
    print(nums)

