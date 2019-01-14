from collections import Counter

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s:
            return ""
        t_dict, count_dict = Counter(t), {}
        ls, required = len(s), len(t_dict)
        l, r = 0, 0
        formed = 0
        ans = ()
        while r < ls:
            character = s[r]
            count_dict[character] = count_dict.get(character, 0) + 1
            if count_dict[character] == t_dict[character]:
                formed += 1
            while l <= r and formed == required:
                character = s[l]
                count_dict[character] -= 1
                if count_dict[character] < t_dict[character]:
                    formed -= 1
                    if not ans or (ans and r-l+1 < ans[1]-ans[0]):
                        ans = (l, r+1)
                l += 1
            r += 1
        return "" if not ans else s[ans[0]:ans[1]]


if __name__ == '__main__':
    S = "aa"
    T = "aa"
    finder = Solution()
    res = finder.minWindow(S, T)
    print(res)

