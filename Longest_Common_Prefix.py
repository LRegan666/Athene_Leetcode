class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        short_num, shortest_str = float('inf'), ''
        status = False
        tagged_length = 0
        for s in strs:
            if len(s) < short_num:
                short_num = len(s)
                shortest_str = s
        if shortest_str == '':
            return ''
        strs.remove(shortest_str)
        for i in range(short_num):
            for item in strs:
                if item[i] == shortest_str[i]:
                    continue
                else:
                    status = True
                    break
            if status or i == short_num-1:
                tagged_length = i
                break
        short_end_strs = list(set([item[short_num-1] for item in strs]))
        if tagged_length == short_num-1 and strs[0][short_num-1] == shortest_str[tagged_length] \
                and len(short_end_strs) == 1:
            return shortest_str
        else:
            return shortest_str[:tagged_length]


if __name__ == '__main__':
    s = ['a', 'a', 'b']
    prefix_collector = Solution()
    res = prefix_collector.longestCommonPrefix(s)
    print(res)