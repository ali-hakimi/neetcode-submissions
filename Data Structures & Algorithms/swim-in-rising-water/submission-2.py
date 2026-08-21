class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        minHeap = [[grid[0][0], 0, 0]]
        visit = set()

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if (r, c) == (ROWS - 1, COLS - 1):
                return t
            for dr, dc in dirs:
                newRow, newCol = r + dr, c + dc
                if (
                    not (0 <= newRow < ROWS)
                    or not (0 <= newCol < COLS)
                    or (newRow, newCol) in visit
                ):
                    continue
                minTime = max(grid[newRow][newCol], t)
                heapq.heappush(minHeap, [minTime, newRow, newCol])
                visit.add((newRow, newCol))
