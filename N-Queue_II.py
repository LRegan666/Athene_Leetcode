class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        res = []
        if n >= 4:
            self.queue(n, res)
        return len(res)

    def queue(self, N, res, state=()):
        ls = len(state)
        for pos in range(N):
            if not self.conflict(state, pos):
                if ls == N-1:
                    res.append(1)
                    return
                else:
                    self.queue(N, res, state+(pos,))

    def conflict(self, state, pos):
        ls = len(state)
        for i in range(ls):
            if state[i] == pos or abs(pos-state[i]) == ls-i:
                return True
        return False


if __name__ == '__main__':
    n = 4
    computer = Solution()
    res = computer.totalNQueens(n)
    print(res)
