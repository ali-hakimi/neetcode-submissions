class Solution {
    public boolean exist(char[][] board, String word) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == word.charAt(0)) {
                    if (dfs(i, j, board, 1, word)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
    private boolean dfs(int i, int j, char[][] board, int idx, String word) {
        if (idx == word.length()) {
            return true;
        }
        System.out.println("ij: " + i + " " + j);

        char temp = board[i][j];
        System.out.println(temp);
        board[i][j] = '#';
        int[][] dirs = new int[][] {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
        for (int[] dir : dirs) {
            int r = i + dir[0];
            int c = j + dir[1];
            if (r >= board.length || c >= board[0].length || r < 0 || c < 0) {
                continue;
            }
            System.out.println(r + " " + c);
            if (board[r][c] == word.charAt(idx) && dfs(r, c, board, idx + 1, word)) {
                return true;
            }
        }
        board[i][j] = temp;
        return false;
    }
}