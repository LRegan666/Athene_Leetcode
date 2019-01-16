class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        tmp, res =[], []
        for k in range(len(nums)+1):
            self.search_subset(nums, k, tmp, res)
        return res

    def search_subset(self, nums, k, tmp, res):
        if len(tmp) == k:
            tmp.sort()
            if tmp not in res:
                res.append(tmp)
            return
        if not nums:
            return
        for i in range(len(nums)):
            self.search_subset(nums[i+1:], k, tmp+[nums[i]], res)


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8,10,0]
    finder = Solution()
    res = finder.subsetsWithDup(nums)
    print(res)

