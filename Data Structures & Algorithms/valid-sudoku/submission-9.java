class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Character>[] rows = new HashSet[9];
        Set<Character>[] cols = new HashSet[9];
        Set<Character>[] boxes = new HashSet[9];

        for (int i = 0; i < 9; i++) {
            rows[i] = new HashSet<>();
            cols[i] = new HashSet<>();
            boxes[i] = new HashSet<>();
        }

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char c = board[i][j];
                if (c == '.') {
                    continue;
                }
                if (!rows[i].add(c)) {
                    System.out.println("row");
                    return false;
                }
                if (!cols[j].add(c)) {
                    System.out.println("col");

                    return false;
                }
                int boxIdx = (i / 3) * 3 + (j / 3);
                if (!boxes[boxIdx].add(c)) {
                    System.out.println("box");

                    return false;
                }
            }
        }
        return true;
    }
}
