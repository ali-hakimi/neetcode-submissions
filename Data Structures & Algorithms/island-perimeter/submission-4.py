class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0

            visit.add((i, j))
            count = 0
            count += dfs(i + 1, j)
            count += dfs(i - 1, j)
            count += dfs(i, j + 1)
            count += dfs(i, j - 1)
            return count
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return dfs(i,j)
                    
