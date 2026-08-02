class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl, pac = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visit, prev):
            if not (0 <= r < ROWS) or not (0 <= c < COLS):
                return
            m = heights[r][c]
            if m < prev or (r, c) in visit:
                return

            visit.add((r, c))
            dfs(r + 1, c, visit, m)
            dfs(r - 1, c, visit, m)
            dfs(r, c + 1, visit, m)
            dfs(r, c - 1, visit, m)

        for i in range(ROWS):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, COLS - 1, atl, heights[i][COLS - 1])

        for i in range(COLS):
            dfs(0, i, pac, heights[0][i])
            dfs(ROWS - 1, i, atl, heights[ROWS - 1][i])
        
        res = atl & pac

        return [list(item) for item in res]
        