class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        dfs(res, new ArrayList<>(), 0, nums);
        return res;
    }
    private void dfs(List<List<Integer>> res, List<Integer> subset, int start, int[] nums) {
        res.add(new ArrayList<>(subset));
        for (int i = start; i < nums.length; i++) {
            if (i > start && nums[i] == nums[i - 1]) {
                continue;
            }
            subset.add(nums[i]);
            dfs(res, subset, i + 1, nums);
            subset.remove(subset.size() - 1);
        }
    }
}

