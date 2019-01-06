class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 1
        for num in range(1, len(nums)+1):
            try:
                nums.remove(num)
                counter += 1
            except:
                return num
        return counter


if __name__ == '__main__':
    nums = [7,8,9,11,12]
    finder = Solution()
    res = finder.firstMissingPositive(nums)
    print(res)
