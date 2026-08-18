class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append([i, j])

        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        time = 0
        while q:
            lenQ = len(q)
            addTime = False
            for _ in range(lenQ):
                r, c = q.popleft()
                for dr, dc in dirs:
                    row, col = r + dr, c + dc
                    if not (0 <= row < ROWS) or not (0 <= col < COLS):
                        continue
                    if grid[row][col] != 1:
                        continue
                    addTime = True
                    grid[row][col] = 2
                    q.append([row, col])
            if addTime:
                time+=1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return time
