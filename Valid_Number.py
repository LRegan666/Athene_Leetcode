class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        s = s.strip()
        if ' ' in s:
            return False
        num_strings = tuple([str(i) for i in range(10)])
        valid_strings = num_strings + ('e', '-', '+', '.')
        for c in s:
            if c not in valid_strings:
                return False
        if 'e' in s:
            if s == 'e':
                return False
            sub_strings = s.split('e')
            if len(sub_strings) > 2:
                return False
            if len(sub_strings) == 2:
                return (self.valid_integer(sub_strings[0], num_strings)
                        or self.valid_float(sub_strings[0], num_strings)) \
                       and self.valid_integer(sub_strings[1], num_strings)
        return self.valid_integer(s, num_strings) or self.valid_float(s, num_strings)

    def valid_integer(self, s, num_strings):
        if not s:
            return False
        if s[0] in ('-', '+'):
            if len(s) == 1:
                return False
            if s[1] in num_strings:
                for c in s[2:]:
                    if c in ('.', '-', '+'):
                        return False
                return True
            return False
        if s[0] in num_strings:
            if len(s) == 1:
                return True
            for c in s[1:]:
                if c in ('.', '-', '+'):
                    return False
            return True
        return False

    def valid_float(self, s, num_strings):
        if not s:
            return False
        if '.' in s:
            cache_strings = s.split('.')
            if len(cache_strings) > 2:
                return False
            if len(cache_strings) == 2:
                if cache_strings[0] == '' or cache_strings[0] in ('-', '+'):
                    if cache_strings[1] != '':
                        for c in cache_strings[1]:
                            if c not in num_strings:
                                return False
                        return True
                    return False
                else:
                    if self.valid_integer(cache_strings[0], num_strings):
                        for c in cache_strings[1]:
                            if c not in num_strings:
                                return False
                        return True
                    return False
        return False


if __name__ == '__main__':
    s = ". 1"
    pattern_checker = Solution()
    print(pattern_checker.isNumber(s))

