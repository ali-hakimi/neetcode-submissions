class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        backtrack("", 0, 0, n, res);
        return res;
    }
    private void backtrack(String sub, int o, int c, int n, List<String> res) {
        if (o > n || o < c) {
            return;
        }
        if (c == n) {
            res.add(new String(sub));
            return;
        }

        backtrack(sub + "(", o + 1, c, n, res);
        backtrack(sub + ")", o, c + 1, n, res);
    }
}
