class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        //PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> a - b);

        for (int stone: stones) {
            pq.offer(stone);
        }

        while (pq.size() > 1) {
            int stoneA = pq.poll();
            int stoneB = pq.poll();
            if (stoneA != stoneB) {
                pq.offer(Math.abs(stoneA - stoneB));
            }
        }
        return pq.size() > 0 ? pq.poll(): 0;
    }
}
