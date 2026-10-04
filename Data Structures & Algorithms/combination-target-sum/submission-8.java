class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(nums, target, 0, 0, new ArrayList<>(), res);
        return res;
    }

    private void dfs(
        int[] nums, int target, int i, int sum, List<Integer> subset, List<List<Integer>> res) {
        if (sum == target) {
            res.add(new ArrayList<>(subset));
            return;
        }
        if (i >= nums.length || sum > target) {
            return;
        }
        subset.add(nums[i]);
        sum += nums[i];
        dfs(nums, target, i, sum, (subset), res);
        subset.remove(subset.size() - 1);
        sum -= nums[i];
        dfs(nums, target, i + 1, sum, (subset), res);
    }
}
