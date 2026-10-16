class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(i, j, prev, visit):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or (i, j) in visit or prev > heights[i][j]:
                return
            visit.add((i, j))
            dfs(i + 1, j, heights[i][j], visit)
            dfs(i - 1, j, heights[i][j], visit)
            dfs(i, j + 1, heights[i][j], visit)
            dfs(i, j - 1, heights[i][j], visit)

        for i in range(ROWS):
            dfs(i, 0, -1, pac)
            dfs(i, COLS - 1, -1, atl)
        
        for j in range(COLS):
            dfs(0, j, -1, pac)
            dfs(ROWS -1, j, -1, atl)

        return [[a, b] for a, b in (pac & atl)]