class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c, prevVal):
            if not (0 <= r < ROWS) or not (0 <= c < COLS) or matrix[r][c] <= prevVal:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            
            res = 1
            res = max(res,1 + dfs(r+1,c, matrix[r][c]))
            res = max(res,1 + dfs(r-1,c, matrix[r][c]))
            res = max(res,1 + dfs(r,c+1, matrix[r][c]))
            res = max(res,1 + dfs(r,c-1, matrix[r][c]))
            dp[(r,c)] = res
            return res

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j,-1)
        return max(dp.values())