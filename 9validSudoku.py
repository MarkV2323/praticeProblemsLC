"""
Author: Mark Vincent II
For LeetCode problem: https://leetcode.com/problems/valid-sudoku/submissions/
Problem Statement:
Given a Sudoku board, check if it's valid or not.

Problem Solution:
"""
class Solution:

    @staticmethod
    def is_valid_sudoku(board: list[list[str]]) -> bool:
        # build lists containing sets for each row, column and square.
        rows = [set() for i in range(0, 9)]
        cols = [set() for i in range(0, 9)]
        squares = [set() for i in range(0, 9)]

        # iterate through board
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                cur_cell = board[i][j]
                # skip over blanks
                if cur_cell == '.':
                    continue
                # get squares set index.
                squares_index = ((i//3) * 3) + (j//3)

                # check if cell exists in sets already
                if (cur_cell in rows[i]) or (cur_cell in cols[j]) or (cur_cell in squares[squares_index]):
                    return False
                # add cell to sets.
                rows[i].add(cur_cell)
                cols[j].add(cur_cell)
                squares[squares_index].add(cur_cell)

        return True


b1 = \
 [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

b2 = \
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

sol = Solution()
valid1 = sol.is_valid_sudoku(b1)
valid2 = sol.is_valid_sudoku(b2)
print(f"{valid1} and {valid2}")
