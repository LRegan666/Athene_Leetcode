class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 1:
            return [['Q']]
        res = []
        if n >= 4:
            queue_group = list(self.queue(n))
            for q in queue_group:
                tmp = []
                for i in q:
                    current_line = '.'*i + 'Q' + '.'*(n-1-i)
                    tmp.append(current_line)
                res.append(tmp)
        return res

    def queue(self, N, state=()):
        ls = len(state)
        for pos in range(N):
            if not self.conflict(state, pos):
                if ls == N-1:
                    yield (pos,)
                else:
                    for result in self.queue(N, state+(pos,)):
                        yield (pos,)+result

    def conflict(self, state, pos):
        ls = len(state)
        for i in range(ls):
            if state[i] == pos or abs(pos-state[i]) == ls-i:
                return True
        return False


if __name__ == '__main__':
    n = 4
    generator = Solution()
    res = generator.solveNQueens(n)
    print(res)
