class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(r, c):
            q = deque([(r, c)])
            visit.add((r, c))
            perm = 0
            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    row = x + dx
                    col = y + dy
                    if not (0 <= row < ROWS) or not (0 <= col < COLS) or grid[row][col] == 0:
                        perm += 1
                    elif (row, col) not in visit:
                        visit.add((row, col))
                        q.append((row, col))
            return perm

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return bfs(i, j)
        return 0
