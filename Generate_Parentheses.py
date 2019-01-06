"""
class Solution:
    def generateParenthesis(self, n):
        # :type n: int
        # :rtype: List[str]
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - 1 - c):
                    ans.append('{}({})'.format(left, right))
        return ans
"""

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def collectParenthesis(left, right, res=''):
            if len(res) == 2*n:
                ans.append(res)
                return
            if left < n:
                collectParenthesis(left+1, right, res+'(')
            if right < left:
                collectParenthesis(left, right+1, res+')')
        collectParenthesis(0, 0)
        return ans


if __name__ == '__main__':
    N = 3
    generator = Solution()
    res = generator.generateParenthesis(N)
    print(res)
