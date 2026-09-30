class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int res = n + 1;
        int l = 0, r = 0;
        int curSum = 0;
        while (r < n) {
            curSum += nums[r];
            while (curSum >= target) {
                res = Math.min(res, r - l + 1);
                curSum -= nums[l];
                l++;
            }
            r++;
        }
        return res == n + 1 ? 0 : res;
    }
}