class Solution {
    public int minimumEffortPath(int[][] heights) {
        int ROWS = heights.length;
        int COLS = heights[0].length;
        int[][] dirs = new int[][] {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[2], b[2]));
        boolean[][] visited = new boolean[ROWS][COLS];
        pq.offer(new int[] {0, 0, 0}); // {row, col, cur max diff}

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int r = cur[0], c = cur[1];

            if (r == ROWS - 1 && c == COLS - 1) {
                return cur[2];
            }
            if (visited[r][c]) {
                continue;
            }
            visited[r][c] = true;
            for (int[] dir : dirs) {
                int newRow = dir[0] + r;
                int newCol = dir[1] + c;

                if (newRow < 0 || newCol < 0 || newRow >= ROWS || newCol >= COLS) {
                    continue;
                }
                int newEffort = Math.max(cur[2], Math.abs(heights[newRow][newCol] - heights[r][c]));
                pq.offer(new int[] {newRow, newCol, newEffort});
            }
            System.out.println(Arrays.toString(pq.peek()));
        }
        return 0;
    }
}