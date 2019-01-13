class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        path = path.split('/')
        for d in path:
            if d == '' or d == '.':
                continue
            elif d == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        return '/' + '/'.join(stack)


if __name__ == '__main__':
    path = "/a//b////c/d//././/.."
    filter = Solution()
    res = filter.simplifyPath(path)
    print(res)



