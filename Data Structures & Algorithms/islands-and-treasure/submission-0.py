class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, dist):
            if not (0 <= r < ROWS) or not (0 <= c < COLS):
                return
            if grid[r][c] == 0 or grid[r][c] == -1:
                return 
            print("hi")
            if grid[r][c] < dist:
                return
            grid[r][c] = min(grid[r][c], dist)

            dfs(r+1, c, dist + 1)
            dfs(r-1, c, dist + 1)
            dfs(r, c+1, dist + 1)
            dfs(r, c-1, dist + 1)


        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    dfs(r+1, c, 1)
                    dfs(r-1, c, 1)
                    dfs(r, c+1, 1)
                    dfs(r, c-1, 1)
        return