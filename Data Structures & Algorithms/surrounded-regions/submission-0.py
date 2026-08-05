class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque()

        for r in range(ROWS):
            if board[r][0] == "O":
                q.append([r, 0])
            if board[r][COLS - 1] == "O":
                q.append([r, COLS - 1])

        for c in range(1, COLS - 1):
            if board[0][c] == "O":
                q.append([0, c])
            if board[ROWS - 1][c] == "O":
                q.append([ROWS - 1, c])

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                board[r][c] = "S"
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                        continue
                    if board[row][col] != "O":
                        continue
                    q.append([row, col])
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = "X"
                if board[r][c] == 'S':
                    board[r][c] = "O"
                



