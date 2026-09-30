class NumMatrix {
    private static int[][] matrix;
    public NumMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (i > 0) {
                    matrix[i][j] += matrix[i - 1][j];
                }
                if (j > 0) {
                    matrix[i][j] += matrix[i][j - 1];
                }
                if (i > 0 && j > 0) {
                    matrix[i][j] -= matrix[i-1][j-1];
                }
            }
        }
        this.matrix = matrix;
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        int res = matrix[row2][col2];
        if (row1 > 0 && col1 > 0) {
            res += matrix[row1 - 1][col1 - 1];
        }
        if (row1 > 0) {
            res -= matrix[row1 - 1][col2];
        }
        if (col1 > 0) {
            res -= matrix[row2][col1 - 1];
        }
        return res;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */