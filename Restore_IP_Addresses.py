class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4:
            return []
        tmp, rec = [], []
        self.generate_ip(s, tmp, rec)
        return rec

    def generate_ip(self, s, tmp, rec):
        if len(tmp) > 4:
            return
        if not s:
            if len(tmp) == 4:
                rec.append('.'.join(tmp))
            return
        if 0 <= int(s[0]) < 10:
            self.generate_ip(s[1:], tmp+[s[0]], rec)
        if len(s) > 1 and 10 <= int(s[:2]) < 100:
            self.generate_ip(s[2:], tmp+[s[:2]], rec)
        if len(s) > 2 and s[0] != '0' and 100 <= int(s[:3]) <= 255:
            self.generate_ip(s[3:], tmp+[s[:3]], rec)


if __name__ == '__main__':
    s = "25525511135"
    res = Solution().restoreIpAddresses(s)
    print(res)
