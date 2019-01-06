import random
import numpy as np


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rows, columns, cubes = {}, {}, {}
        node = []
        for i in range(9):
            rows[i] = set([str(num) for num in range(1, 10)])
            for j in range(9):
                ind = int(i / 3) * 3 + int(j / 3)
                columns[j] = columns.get(j, set([str(num) for num in range(1, 10)]))
                cubes[ind] = cubes.get(ind, set([str(num) for num in range(1, 10)]))
                if board[i][j] != '.':
                    rows[i].remove(board[i][j])
                    columns[j].remove(board[i][j])
                    cubes[ind].remove(board[i][j])
                else:
                    node.append((i, j))
        self.solver(board, rows, columns, cubes, node, 0, len(node))

    def solver(self, board, rows, columns, cubes, node, start, end):
        if start == end:
            return True
        i, j = node[start][0], node[start][1]
        ind = int(i / 3) * 3 + int(j / 3)
        for num in list(rows[i]):
            if num not in columns[j] or num not in cubes[ind]:
                continue
            else:
                rows[i].remove(num)
                columns[j].remove(num)
                cubes[ind].remove(num)
                board[i][j] = num
                if self.solver(board, rows, columns, cubes, node, start+1, end):
                    return True
                else:
                    rows[i].add(num)
                    columns[j].add(num)
                    cubes[ind].add(num)
                    board[i][j] = '.'
        return False


if __name__ == '__main__':
    board = []
    print(np.mat(board))
    print('=======================================')
    filler = Solution()
    filler.solveSudoku(board)
    print(np.mat(board))

