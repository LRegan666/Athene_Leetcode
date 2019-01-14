class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        tmp, res = [], []
        L = len(nums)
        for k in range(L+1):
            self.combination_search(nums, k, tmp, res)
        return res

    def combination_search(self, nums, k, tmp, res):
        if len(tmp) == k:
            res.append(tmp)
            return
        L = len(nums)
        for i in range(L):
            self.combination_search(nums[i+1:], k, tmp+[nums[i]], res)


if __name__ == '__main__':
    nums = [1,2,3]
    finder = Solution()
    res = finder.subsets(nums)
    print(res)

