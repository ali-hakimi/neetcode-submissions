class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        minHeap = [[grid[0][0], 0, 0]]
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])

        while minHeap:
            cost, x, y = heapq.heappop(minHeap)
            if (x, y) == (ROWS - 1, COLS - 1):
                return cost
            if (x, y) in visit:
                continue
            visit.add((x, y))
            for dx, dy in dirs:
                row, col = x + dx, y + dy
                if not (0 <= row < ROWS) or not (0 <= col < COLS) or (row, col) in visit:
                    continue
                maxDist = max(cost, grid[row][col])
                heapq.heappush(minHeap, [maxDist, row, col])
            
