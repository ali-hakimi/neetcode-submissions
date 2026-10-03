class Solution {
    public String longestDiverseString(int a, int b, int c) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((x, y) -> Integer.compare(y[0], x[0]));
        if (a > 0)
            pq.offer(new int[] {a, 0});
        if (b > 0)
            pq.offer(new int[] {b, 1});
        if (c > 0)
            pq.offer(new int[] {c, 2});

        StringBuilder sb = new StringBuilder();
        int prev1 = -1, prev2 = -2;
        while (!pq.isEmpty()) {
            int[] ar = pq.poll();
            char char1 = (char) (ar[1] + 'a');
            int count1 = ar[0];
            if (char1 == prev1 && char1 == prev2) {
                if (pq.isEmpty()) {
                    break;
                }
                int[] ar2 = pq.poll();
                char char2 = (char) (ar2[1] + 'a');
                int count2 = ar2[0];
                sb.append(char2);
                count2--;
                if (count2 > 0) {
                    pq.offer(new int[] {count2, ar2[1]});
                }
                prev2 = prev1;
                prev1 = char2;
            }
            sb.append(char1);
            count1--;
            if (count1 > 0) {
                pq.offer(new int[] {count1, ar[1]});
            }
            prev2 = prev1;
            prev1 = char1;
        }
        return sb.toString();
    }
}