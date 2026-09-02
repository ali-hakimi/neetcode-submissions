class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        minHeap = [[0, 0, 0]]

        visited = set()
        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if (r, c) == (ROWS - 1, COLS - 1):
                return diff
            for dr, dc in dirs:
                newRow = dr + r
                newCol = dc + c
                if (
                    not (0 <= newRow < ROWS)
                    or not (0 <= newCol < COLS)
                    or (newRow, newCol) in visited
                ):
                    continue
                newDiff = abs(heights[newRow][newCol] - heights[r][c])
                heapq.heappush(minHeap, [max(diff, newDiff), newRow, newCol])