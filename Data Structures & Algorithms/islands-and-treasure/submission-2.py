class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append([i, j])

        dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                row, col = r + dr, c + dc
                if not (0 <= row < ROWS) or not (0 <= col < COLS):
                    continue
                if grid[row][col] != 2**31 - 1:
                    continue

                grid[row][col] = grid[r][c] + 1
                q.append([row, col])