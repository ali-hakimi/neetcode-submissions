class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> sublist = new ArrayList<>();
        dfs(1, sublist, res, n, k);
        return res;
    }
    private void dfs(int start, List<Integer> sublist, List<List<Integer>> res, int n, int k) {
        if (sublist.size() == k) {
            res.add(new ArrayList<>(sublist));
        }
        for (int i = start; i <= n; i++) {
            sublist.add(i);
            dfs(i + 1, sublist, res, n, k);
            sublist.remove(sublist.size() - 1);
        }
    }
}