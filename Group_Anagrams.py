class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_dict = {}
        for s in strs:
            current_key = ''.join(sorted(s))
            if current_key not in str_dict:
                str_dict[current_key] = []
            str_dict[current_key].append(s)
        return list(str_dict.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    finder = Solution()
    res = finder.groupAnagrams(strs)
    print(res)
