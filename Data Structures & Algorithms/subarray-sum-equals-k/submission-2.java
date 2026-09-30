class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == k) {
                // count += 1;
            }
            if (i > 0) {
                nums[i] += nums[i - 1];
            }
        }
        System.out.println(Arrays.toString(nums));
        System.out.println("_______________");

        for (int i = nums.length - 1; i >= 0; i--) {
            for (int j = i - 1; j >= 0; j--) {
                if (nums[i] - nums[j] == k) {
                    count += 1;
                    System.out.println(i + " " + j);
                }
            }

            if (nums[i] == k) {
                count += 1;
            }
        }

        return count;
    }
}