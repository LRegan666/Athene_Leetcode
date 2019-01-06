class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        check_status = False
        characters = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '.')
        for i in range(9):
            cnum = 0
            for item in board[i]:
                if item not in characters:
                    check_status = True
                    break
                if item != characters[-1]:
                    cnum += 1
            if check_status:
                break
            if len(set(board[i])) != cnum + 1:
                check_status = True
                break
        if not check_status:
            for j in range(9):
                tmp = []
                for k in range(9):
                    if board[k][j] not in characters:
                        check_status = True
                        break
                    if board[k][j] != characters[-1]:
                        if board[k][j] not in tmp:
                            tmp.append(board[k][j])
                        else:
                            check_status = True
                            break
                if check_status:
                    break
        if not check_status:
            for rs in (0, 3, 6):
                for cs in (0, 3, 6):
                    tmp = []
                    for r in range(rs, rs+3):
                        for c in range(cs, cs+3):
                            if board[r][c] not in characters:
                                check_status = True
                                break
                            if board[r][c] != characters[-1]:
                                if board[r][c] not in tmp:
                                    tmp.append(board[r][c])
                                else:
                                    check_status = True
                                    break
                        if check_status:
                            break
                    if check_status:
                        break
                if check_status:
                    break
        return not check_status


if __name__ == '__main__':
    board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    judger = Solution()
    res = judger.isValidSudoku(board)
    print(res)

