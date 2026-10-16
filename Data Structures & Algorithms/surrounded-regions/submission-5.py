class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or board[i][j] != "O":
                return
            board[i][j] = "#"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for i in range(ROWS):
            dfs(i, 0)
            dfs(i, COLS -1)
        
        for i in range(COLS):
            dfs(0, i)
            dfs(ROWS - 1, i)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
            