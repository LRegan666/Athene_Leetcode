from collections import defaultdict

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = defaultdict(set)
        cand_count = {}
        for cand in set(candidates):
            if cand <= target:
                dp[cand].add((cand,))
            cand_count[cand] = candidates.count(cand)
        for cand in candidates:
            for item in range(cand, target+1):
                prev = dp[item-cand]
                for t in prev:
                    new_t = tuple(sorted(t+(cand,)))
                    if new_t.count(cand) <= cand_count[cand]:
                        if new_t not in dp[item]:
                            dp[item].add(new_t)
        return dp[target]

    def combination_execise(self, candidates, target):
        dp = defaultdict(set)
        candidate_count = {}
        for candidate in candidates:
            if candidate <= target:
                dp[candidate].add((candidate,))
                candidate_count[candidate] = candidates.count(candidate)
        for candidate in candidates:
            for item in range(candidate, target+1):
                prev = dp[item-candidate]
                for t in prev:
                    new_t = tuple(sorted(t+(candidate,)))
                    if new_t.count(candidate) <= candidate_count[candidate]:
                        dp[item].add(new_t)
        return [list(item) for item in dp[target]]


if __name__ == '__main__':
    candidates = [14,18,19,30,6,5,14,23,28,18,26,21,12,15,29,18,32,23,6,21,19,30,6,28,17,13,29,28,10,34,26,11,10,32,
                  7,11,32,8,21,18,22,5,34,21,7,20,26,5,9,28,21,23,23,15,8,27,23,32,12,20,31,33,27,28,30,21,34,19]
    target = 29
    combinator = Solution()
    res = combinator.combination_execise(candidates, target)
    print(res)
