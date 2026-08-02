class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int, idx: int) -> bool:
            # Found the entire word
            if idx == len(word):
                return True

            # Out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # Already visited or character doesn't match
            if board[r][c] == "#" or board[r][c] != word[idx]:
                return False

            # Mark as visited
            char = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r, c + 1, idx + 1) or  # Right
                dfs(r, c - 1, idx + 1) or  # Left
                dfs(r + 1, c, idx + 1) or  # Down
                dfs(r - 1, c, idx + 1)     # Up
            )

            # Restore the cell
            board[r][c] = char

            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False