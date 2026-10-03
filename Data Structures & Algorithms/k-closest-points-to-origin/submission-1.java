class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        for (int[] p: points) {
            int dst = (p[0] * p[0] + p[1] * p[1]);
            pq.offer(new int[]{dst, p[0], p[1]});
        }

        int[][] res = new int[k][2];
        for (int i = 0; i < k; i++) {
            int[] p = pq.poll();
            res[i][0] = p[1];
            res[i][1] = p[2];
        }
        return res;
    }
}
