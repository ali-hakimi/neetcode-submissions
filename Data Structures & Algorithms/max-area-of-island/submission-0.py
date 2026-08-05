class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if not (0 <= r < ROWS) or not (0 <= c < COLS):
                return 0
            if grid[r][c] != 1:
                return 0
            
            grid[r][c] = -1

            count = 1
            count += dfs(r+1, c)
            count += dfs(r-1, c)
            count += dfs(r, c+1)
            count += dfs(r, c-1)
            return count
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    count = dfs(r, c)
                    maxArea = max(maxArea, count)
                    print("hi")
        
        dfs(0,0)
        return maxArea