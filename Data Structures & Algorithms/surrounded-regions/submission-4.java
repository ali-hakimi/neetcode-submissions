class Solution {
    public void solve(char[][] board) {
        int ROW = board.length;
        int COL = board[0].length;
        Queue<int[]> q = new LinkedList<>();

        for (int i = 0; i < ROW; i++) {
            if (board[i][0] == 'O') {
                q.offer(new int[] {i, 0});
            }
            if (board[i][COL - 1] == 'O') {
                q.offer(new int[] {i, COL - 1});
            }
        }

        for (int i = 0; i < COL; i++) {
            if (board[0][i] == 'O') {
                q.offer(new int[] {0, i});
            }
            if (board[ROW - 1][i] == 'O') {
                q.offer(new int[] {ROW - 1, i});
            }
        }
        int[][] dirs = new int[][] {{0, 1}, {-1, 0}, {1, 0}, {0, -1}};

        while (!q.isEmpty()) {
            int[] rc = q.poll();
            board[rc[0]][rc[1]] = 'T';
            for (int[] dr : dirs) {
                int r = rc[0] + dr[0];
                int c = rc[1] + dr[1];
                if (r < 0 || c < 0 || r >= ROW || c >= COL || board[r][c] == 'X'
                    || board[r][c] == 'T') {
                    continue;
                }
                q.offer(new int[] {r, c});
            }
        }

        for (int i = 0; i < ROW; i++) {
            for (int j = 0; j < COL; j++) {
                if (board[i][j] == 'T') {
                    board[i][j] = 'O';
                } else if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
            }
        }
    }
}
