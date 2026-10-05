class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int totalSum = Arrays.stream(nums).sum();
        if (totalSum % k != 0 || nums.length < k) {
            return false;
        }
        Arrays.sort(nums);
        int length = totalSum / k;
        int[] subs = new int[k];

        return dfs(nums, subs, nums.length, k, length);
    }

    private boolean dfs(int[] nums, int[] subs, int idx, int k, int length) {
        if (idx == 0) {
            return true;
        }

        for (int i = 0; i < k; i++) {
            if (subs[i] + nums[idx - 1] <= length) {
                subs[i] += nums[idx - 1];
                if (dfs(nums, subs, idx - 1, k, length))
                    return true;
                subs[i] -= nums[idx - 1];
            }

            if (subs[i] == 0) {
                break;
            }
        }
        return false;
    }
}