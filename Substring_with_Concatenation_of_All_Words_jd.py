class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        freq = {}
        for word in words:
            if word not in freq:
                freq[word] = 0
            freq[word] += 1
        ls = len(s)
        lm, ln = len(words[0]), len(words)
        res = []
        for i in range(ls-lm*ln+1):
            current_string = s[i:i+lm*ln]
            if self.valid_concatenation(current_string, lm, ln, freq):
                res.append(i)
        return res

    def valid_concatenation(self, s, lm, ln, fq):
        f = {}
        j, n = 0, len(fq)
        while j < lm*ln and n > 0:
            word = s[j:j+lm]
            if word not in fq:
                break
            if word not in f:
                f[word] = 0
            f[word] += 1
            if f[word] > fq[word]:
                break
            if f[word] == fq[word]:
                n -= 1
            j += lm
        return n == 0


if __name__ == '__main__':
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "good"]
    finder = Solution()
    res = finder.findSubstring(s, words)
    print(res)