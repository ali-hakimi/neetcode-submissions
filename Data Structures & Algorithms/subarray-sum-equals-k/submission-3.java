class Solution {
    public int subarraySum(int[] nums, int k) {
        int curSum = 0;
        int total = 0;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);

        for(int n: nums) {
            curSum += n;
            int diff = curSum - k;
            total += map.getOrDefault(diff, 0);
            map.put(curSum, map.getOrDefault(curSum, 0) + 1);
        }
        return total;

    }
}