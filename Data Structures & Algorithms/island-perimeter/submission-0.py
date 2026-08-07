class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        per = 0

        def dfs(r, c):
            nonlocal per
            if not (0 <= r < ROWS) or not (0 <= c < COLS):
                per += 1
                return
            if grid[r][c] == 0:
                per += 1
                return 
            if grid[r][c] == -1:
                return
            grid[r][c] = -1

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)

        return per