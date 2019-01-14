class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < 1 or n < k:
            return []
        nums = list(range(1, n+1))
        tmp, res = [], []
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
    n, k = 4, 2
    combiner = Solution()
    res = combiner.combine(n, k)
    print(res)

