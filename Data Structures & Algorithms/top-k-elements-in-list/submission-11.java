class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int n = nums.length;
        int[] res = new int[k];
        List<Integer>[] freq = new List[n + 1];
        for (int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }

        Map<Integer, Integer> count = new HashMap<>();
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        for(Map.Entry<Integer, Integer> entry: count.entrySet()) {
            freq[entry.getValue()].add(entry.getKey());
        }

        for (int i = freq.length - 1; i > 0; i--) {
            for (int key : freq[i]) {
                res[--k] = key;
                if (k <= 0) {
                    return res;
                }
            }
        }
        return res;

    }
}
