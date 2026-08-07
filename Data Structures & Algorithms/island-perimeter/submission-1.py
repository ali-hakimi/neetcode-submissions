class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if not (0 <= r < ROWS) or not (0 <= c < COLS) or grid[r][c] == 0:
                return 1
            if (r, c) in visit:
                return 0
            visit.add((r,c))
            
            return dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)

        return 0