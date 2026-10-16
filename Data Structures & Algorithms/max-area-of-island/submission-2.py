class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            res = 1
            res += dfs(i,j+1)
            res += dfs(i,j-1)
            res += dfs(i+1,j)
            res += dfs(i-1,j)
            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i,j))
        return maxArea