class Solution {
    public int[] sortArray(int[] nums) {
        if (nums.length == 0) {
            return new int[0];
        }
        if (nums.length == 1) {
            return nums;
        }

        int mid = nums.length / 2;
        int[] left = sortArray(Arrays.copyOfRange(nums, 0, mid));
        int[] right = sortArray(Arrays.copyOfRange(nums, mid, nums.length));

        int[] merged = new int[left.length + right.length];

        int i = 0;
        int j = 0;

        while (i < left.length && j < right.length) {
            if (left[i] < right[j]) {
                merged[i + j] = left[i];
                i += 1;
            } else {
                merged[i + j] = right[j];
                j += 1;
            }
        }
        while (i < left.length) {
            merged[i + j] = left[i];
            i += 1;
        }
        while (j < right.length) {
            merged[i + j] = right[j];
            j += 1;
        }
        return merged;
    }
}