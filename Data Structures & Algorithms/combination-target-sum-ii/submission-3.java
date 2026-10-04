class Solution {
    private List<List<Integer>> res;
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        res = new ArrayList<>();
        Arrays.sort(candidates);
        dfs(0, new ArrayList<>(), 0, candidates, target);
        return res;
    }

    public void dfs(int i, List<Integer> sublist, int sum, int[] candidates, int target) {
        if (sum == target) {
            res.add(new ArrayList<>(sublist));
            return;
        }
        for (int j = i; j < candidates.length; j++) {
            if (j > i && candidates[j] == candidates[j-1]){
                continue;
            }
            if (sum + candidates[j] > target) {
                break;
            }
            sublist.add(candidates[j]);
            dfs(j + 1, sublist, sum + candidates[j], candidates, target);
            sublist.remove(sublist.size() - 1);
        }
    }
}
