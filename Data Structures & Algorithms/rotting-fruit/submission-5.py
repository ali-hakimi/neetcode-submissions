class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        if fresh == 0:
            return 0
        
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while q and fresh: 

            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    row = r + dr
                    col = c + dc
                    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                        continue
                    if grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1

        return time if not fresh else -1
