# leetcode 130- surrounded regions

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if(board[r][c] != 'O' or r < 0 or c < 0
                or r >= ROWS or c >=COLS):
                return
            board[r][c] = 'N'
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for i, j in directions:
                row, col = r + i, c + j
                if(row < 0 or col < 0
                    or row >= ROWS or col >=COLS):
                    continue
                if(board[row][col] == 'O'):
                    dfs(row, col)

        # change edge O's and surrounding O's
        for r in range(ROWS):
            if(board[r][0] == 'O'):
                dfs(r, 0)
            if(board[r][COLS - 1] == 'O'):
                dfs(r, COLS - 1)
        for c in range(COLS):
            if(board[0][c] == 'O'):
                dfs(0, c)
            if(board[ROWS - 1][c] == 'O'):
                dfs(ROWS - 1, c)

        # switch O's left to X
        for r in range(ROWS):
            for c in range(COLS):
                if(board[r][c] == 'O'):
                    board[r][c] = 'X'
        
        # switch all N's back to 0's
        for r in range(ROWS):
            for c in range(COLS):
                if(board[r][c] == 'N'):
                    board[r][c] = 'O'

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Solution().solve(board)
print(board)