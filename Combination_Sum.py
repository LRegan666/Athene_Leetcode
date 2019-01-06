class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, tmp = [], []
        self.collector_combination(candidates, target, tmp, res)
        return res

    def collector_combination(self, candidates, target, tmp, res):
        if target == 0:
            tmp.sort()
            if tmp not in res:
                res.append(tmp)
            return
        elif target > 0:
            for candidate in candidates:
                self.collector_combination(candidates, target-candidate, tmp + [candidate], res)
        else:
            return


if __name__ == '__main__':
    candidates = [2,3,5]
    target = 8
    combinator = Solution()
    res = combinator.combinationSum(candidates, target)
    print(res)
