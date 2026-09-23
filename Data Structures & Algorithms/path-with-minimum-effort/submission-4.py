class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        ROWS, COLS = len(heights), len(heights[0])
        minHeap = [[0, 0, 0]]
        visited = set()

        while minHeap:
            diff, x, y = heapq.heappop(minHeap)
            if (x, y) == (ROWS - 1, COLS - 1):
                return diff
            if (x, y) in visited:
                continue
            visited.add((x,y))
            for dr, dc in dirs:
                r = x + dr
                c = y + dc
                if not (0 <= r < ROWS) or not (0 <= c < COLS) or (r, c) in visited:
                    continue
                newDiff = abs(heights[x][y] - heights[r][c])
                heapq.heappush(minHeap, [max(diff, newDiff), r, c])
