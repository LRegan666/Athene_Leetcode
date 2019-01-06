class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if (not s) or (not words):
            return []
        pattern_list, results = [], []
        pattern = ''
        self.words_pattern_collector(words, pattern, pattern_list)
        pattern_list = list(set(pattern_list))
        for p in pattern_list:
            results = self.pattern_compute(s, p, results)
        return results

    def words_pattern_collector(self, w, p, c):
        lw = len(w)
        if lw == 1:
            p = p + w[0]
            c.append(p)
            return
        for i in range(lw):
            t = p + w[i]
            self.words_pattern_collector(w[:i]+w[i+1:], t, c)

    def pattern_compute(self, s, p, r):
        ls, lp = len(s), len(p)
        pi = self.prefix_compute(p)
        k = 0
        for i in range(ls):
            while k > 0 and p[k] != s[i]:
                k = pi[k-1]
            if p[k] == s[i]:
                k += 1
            if k == lp:
                ind = i - k + 1
                r.append(ind)
                k = pi[k-1]
        return r

    def prefix_compute(self, p):
        k, m = 0, len(p)
        pi = [0]*m
        for q in range(1, m):
            while k > 0 and p[k] != p[q]:
                k = pi[k-1]
            if p[k] == p[q]:
                k += 1
            pi[q] = k
        return pi


if __name__ == '__main__':
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    finder = Solution()
    res = []
    finder.pattern_compute(s, "goodgoodbestword", res)
    print(res)

