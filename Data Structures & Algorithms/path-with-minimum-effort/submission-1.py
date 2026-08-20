class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        minHeap = [[0, 0, 0]]
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visit = set()

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            if (r, c) == (ROWS - 1, COLS - 1):
                return diff
            for dr, dc in dirs:
                row, col = r + dr, c + dc
                if not (0 <= row < ROWS) or not (0 <= col < COLS) or (row, col) in visit:
                    continue
                newDiff = abs(heights[r][c]-heights[row][col])
                maxDiff = max(diff, newDiff)
                heapq.heappush(minHeap, [maxDiff, row, col])
            
