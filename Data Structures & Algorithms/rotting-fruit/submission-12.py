class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append([i, j])
                if grid[i][j] == 1:
                    fresh+=1

        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        time = 0
        while q and fresh > 0:
            lenQ = len(q)
            for _ in range(lenQ):
                r, c = q.popleft()
                for dr, dc in dirs:
                    row, col = r + dr, c + dc
                    if not (0 <= row < ROWS) or not (0 <= col < COLS):
                        continue
                    if grid[row][col] != 1:
                        continue
                    fresh -= 1
                    grid[row][col] = 2
                    q.append([row, col])
            time+=1

        return -1 if fresh else time
