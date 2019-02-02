class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    rec = []
                    rec.append((i, j))
                    status = self.word_searcher(board, word[1:], (i, j), rec)
                    if status:
                        return True
        return False

    def word_searcher(self, board, word, pos, rec):
        if not word:
            return True
        if pos[0] != len(board)-1 and board[pos[0]+1][pos[1]] == word[0] and (pos[0]+1, pos[1]) not in rec:
            rec.append((pos[0]+1, pos[1]))
            if self.word_searcher(board, word[1:], (pos[0]+1, pos[1]), rec):
                return True
            rec.remove((pos[0]+1, pos[1]))
        if pos[1] != len(board[0])-1 and board[pos[0]][pos[1]+1] == word[0] and (pos[0], pos[1]+1) not in rec:
            rec.append((pos[0], pos[1]+1))
            if self.word_searcher(board, word[1:], (pos[0], pos[1]+1), rec):
                return True
            rec.remove((pos[0], pos[1]+1))
        if pos[0] != 0 and board[pos[0]-1][pos[1]] == word[0] and (pos[0]-1, pos[1]) not in rec:
            rec.append((pos[0]-1, pos[1]))
            if self.word_searcher(board, word[1:], (pos[0]-1, pos[1]), rec):
                return True
            rec.remove((pos[0]-1, pos[1]))
        if pos[1] != 0 and board[pos[0]][pos[1]-1] == word[0] and (pos[0], pos[1]-1) not in rec:
            rec.append((pos[0], pos[1]-1))
            if self.word_searcher(board, word[1:], (pos[0], pos[1]-1), rec):
                return True
            rec.remove((pos[0], pos[1]-1))
        return False


if __name__ == '__main__':
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word = "ABCB"
    finder = Solution()
    res = finder.exist(board, word)
    print(res)
