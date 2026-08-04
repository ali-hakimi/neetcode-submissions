class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, j, idx):
            if idx == len(word):
                return True
            if not (0 <= i < ROWS) or not (0 <= j < COLS):
                return False
            if board[i][j] != word[idx] or board[i][j] == "#":
                return False

            ch = board[i][j]
            board[i][j] = "#"
            found = (
                dfs(i + 1, j, idx + 1)
                or dfs(i, j + 1, idx + 1)
                or dfs(i - 1, j, idx + 1)
                or dfs(i, j - 1, idx + 1)
            )
            board[i][j] = ch

            return found

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        return False
