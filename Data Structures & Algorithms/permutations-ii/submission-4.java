class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Map<Integer, Integer> count = new HashMap<>();
        for (int n : nums) {
            count.put(n, count.getOrDefault(n, 0) + 1);
        }
        backtrack(new ArrayList<>(), res, count, nums);
        return res;
    }
    private void backtrack(
        List<Integer> sub, List<List<Integer>> res, Map<Integer, Integer> count, int[] nums) {
        if (sub.size() == nums.length) {
            res.add(new ArrayList<>(sub));
            return;
        }

        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            if (entry.getValue() > 0) {
                sub.add(entry.getKey());
                entry.setValue(entry.getValue() - 1);
                backtrack(sub, res, count, nums);
                entry.setValue(entry.getValue() + 1);
                sub.remove(sub.size() - 1);
            }
        }
    }
}