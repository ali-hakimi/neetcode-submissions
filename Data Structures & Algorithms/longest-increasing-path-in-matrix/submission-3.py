import sys
sys.setrecursionlimit(1000000)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        ROWS, COLS = len(matrix), len(matrix[0])
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def dfs(i, j):
            nonlocal cache
            if (i, j) in cache:
                return cache[(i, j)]
            cache[(i, j)] = 1
            for dr, dc in dirs:
                row = dr + i
                col = dc + j
                if (0 <= row < ROWS) and (0 <= col < COLS) and matrix[i][j] < matrix[row][col]:
                    cache[(i,j)] = max(cache[(i, j)], 1 + dfs(row, col))

            return cache[(i, j)]

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j)

        return max(cache.values())
