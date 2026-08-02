class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(i, j):
            if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])) or grid[i][j] == "0":
                return

            grid[i][j] = "0"
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            for direction in dirs:
                row, col = direction[0] + i, direction[1] + j
                dfs(row, col)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count +=1

        return count