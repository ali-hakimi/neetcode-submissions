class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            if not (0 <= r < ROWS) or not (0 <= c < COLS):
                return 
            if grid[r][c] == "#" or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count