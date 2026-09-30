class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int n = nums.length;
        int[] res = new int[k];
        List<Integer>[] count = new List[n + 1];
        for (int i = 0; i <= n; i++) {
            count[i] = new ArrayList<>();
        }
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            count[entry.getValue()].add(entry.getKey());
        }

        k -= 1;
        while (k >= 0) {
            for (int i = 0; i < count[n].size(); i++) {
                res[k] = count[n].get(i);
                k -= 1;
                if (k < 0) {
                    return res;
                }
            }
            n -= 1;
        }
        return res;
    }
}
