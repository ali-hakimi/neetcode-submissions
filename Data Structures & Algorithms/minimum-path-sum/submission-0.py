class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        for r in range(M - 1, -1, -1):
            for c in range(N - 1, -1, -1):
                if r == M - 1 and c == N - 1:
                    continue

                right = grid[r][c + 1] if c + 1 < N else float("inf")
                bot = grid[r + 1][c] if r + 1 < M else float("inf")
                grid[r][c] = grid[r][c] +  min(right, bot)
        return grid[0][0]
