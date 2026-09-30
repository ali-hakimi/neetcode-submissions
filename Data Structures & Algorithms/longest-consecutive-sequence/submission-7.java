class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int n : nums) {
            set.add(n);
        }
        int res = 0;
        for (int n: set) {
            if (set.contains(n-1)) {
                continue;
            }
            int count = 1;
            while (set.contains(n + 1)) {
                count++;
                n++;
            }
            res = Math.max(res, count);
        }
        return res;
    }
}
