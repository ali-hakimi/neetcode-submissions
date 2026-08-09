class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(i, j):
            if not (0 <= i < ROWS) or not (0 <= j < COLS) or grid[i][j] == 0:
                return 1
            if (i,j) in visit:
                return 0
            
            visit.add((i,j))
            perim = 0
            for dr, dc in dirs:
                perim += bfs(i + dr, j + dc)
            return perim

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return bfs(i, j)

        return 0