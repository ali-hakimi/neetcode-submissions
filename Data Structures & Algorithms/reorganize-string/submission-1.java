class Solution {
    public String reorganizeString(String s) {
        int[] count = new int[26];
        for (char c : s.toCharArray()) {
            count[c - 'a']++;
        }
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0]));
        for (int i = 0; i < count.length; i++) {
            if (count[i] > 0) {
                pq.offer(new int[] {count[i], i});
            }
        }
        StringBuilder sb = new StringBuilder();
        int[] spare = null;
        while (!pq.isEmpty()) {
            int[] ar = pq.poll();
            sb.append((char) (ar[1] + 'a'));
            if (spare != null) {
                pq.offer(spare);
                spare = null;
            }
            ar[0]--;
            if (ar[0] > 0) {
                spare = new int[] {ar[0], ar[1]};
            }
        }
        return spare != null ? "" : sb.toString();
    }
}