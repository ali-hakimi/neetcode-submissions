class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))
        level = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if (
                    i < 0
                    or j < 0
                    or i >= ROWS
                    or j >= COLS
                    or grid[i][j] == -1
                    or (grid[i][j] != 2**31 - 1 and level > 0)
                ):
                    continue
                grid[i][j] = level
                q.append((i + 1, j))
                q.append((i - 1, j))
                q.append((i, j + 1))
                q.append((i, j - 1))
            level += 1
