class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()
        fresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        visit = set()
        level = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                i, j = q.popleft()

                for dr, dc in dirs:
                    r, c = i + dr, j + dc
                    if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                        continue
                    q.append((r, c))
                    grid[r][c] = 2
                    fresh -= 1
            level += 1

        return level if fresh == 0 else -1
