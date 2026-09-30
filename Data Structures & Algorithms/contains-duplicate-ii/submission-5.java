class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<>();
        int l = 0, r = 0;
        while (r < nums.length) {
            if (r > k) {
                set.remove(nums[l]);
                l++;
            }
            if (!set.add(nums[r])) {
                return true;
            }
            r++;
        }

        return false;
    }
}