class Solution {
    public int splitArray(int[] nums, int k) {
        int sum = 0;
        int max = 0;
        
        for (int n : nums) {
            sum += n;
            max = Math.max(max, n);
        }

        int res = sum;

        int l = max, r = sum;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (canSplit(nums, k, m)) {
                res = m;
                r = m - 1;
            }
            else {
                l = m + 1;
            }
        }        
        return res;
    }
    private boolean canSplit(int[] nums, int k , int largest) {
        int subArray = 1, curSum = 0;
        for (int n: nums) {
            curSum += n;
            if (curSum > largest) {
                subArray++;
                if (subArray > k) {
                    return false;
                }
                curSum = n;
            }
        }
        return true;
    }
}