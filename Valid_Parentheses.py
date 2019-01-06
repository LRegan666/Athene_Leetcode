class Solution:
    def isValid(self, s):
        """
        symmetric compare
        """
        if not s:
            return True
        stack = []
        for c in s:
            if len(stack) > 0:
                if c == ')' and stack[-1] == '(' or c == '}' and stack[-1] == '{' \
                        or c == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False


if __name__ == '__main__':
    s = "(([]){})"
    determinator = Solution()
    res = determinator.isValid(s)
    print(res)
