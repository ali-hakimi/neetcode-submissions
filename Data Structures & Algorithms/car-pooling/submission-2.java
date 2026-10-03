class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> a[0] == b[0] ? Integer.compare(a[1], b[1]) : Integer.compare(a[0], b[0]));

        for (int[] trip : trips) {
            int passengers = trip[0], start = trip[1], end = trip[2];
            pq.offer(new int[] {start, passengers});
            pq.offer(new int[] {end, -passengers});
        }

        int curPass = 0;
        while (!pq.isEmpty()) {
            int[] point = pq.poll();
            curPass += point[1];
            if (curPass > capacity) {
                return false;
            }
        }
        return true;
    }
}