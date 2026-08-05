class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time = [[float("inf")] * COLS for _ in range(ROWS)]

        def dfs(r, c, t):
            # out of bounds
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return
            
            # empty cell
            if grid[r][c] == 0:
                return

            # if we already found a faster/equal way, stop
            if time[r][c] <= t:
                return
            
            time[r][c] = t

            dfs(r+1, c, t + 1)
            dfs(r-1, c, t + 1)
            dfs(r, c+1, t + 1)
            dfs(r, c-1, t + 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    dfs(r, c, 0)
        
        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    if time[r][c] == float("inf"):
                        return -1
                    ans = max(ans, time[r][c])    
        return ans