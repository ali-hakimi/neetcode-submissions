class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visit, prev):
            if heights[r][c] < prev or (r,c) in visit:
                return
            visit.add((r, c))
            
            h = heights[r][c]
            heights[r][c] = -1
            dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for dr, dc in dirs:
                row, col = r + dr, c + dc
                if not (0 <= row < ROWS) or not (0 <= col < COLS):
                    continue
                dfs(row, col, visit, h)
            heights[r][c] = h

        for r in range(ROWS):
            dfs(r, 0, pac, -1)
            dfs(r, COLS - 1, atl, -1)

        for c in range(COLS):
            dfs(0, c, pac, -1)
            dfs(ROWS - 1, c, atl, -1)

        return [[r,c] for r,c in pac & atl]
