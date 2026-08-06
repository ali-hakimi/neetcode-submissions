class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minH = [[grid[0][0], 0, 0]]
        visit = set()
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while minH:
            t, r, c = heapq.heappop(minH)
            if r == (N - 1) and c == (N - 1):
                return t

            for dr, dc in dirs:
                row = r + dr
                col = c + dc
                if row < 0 or row >= N or col < 0 or col >= N:
                    continue
                if (row, col) in visit:
                    continue
                minHeight = max(t, grid[row][col])
                heapq.heappush(minH, [minHeight, row, col])
                visit.add((row, col))