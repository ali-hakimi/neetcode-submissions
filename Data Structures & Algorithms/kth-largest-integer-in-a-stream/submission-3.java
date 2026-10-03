class KthLargest {

    private PriorityQueue<Integer> pq;
    private int k;
    public KthLargest(int k, int[] nums) {
        this.k = k;
        pq = new PriorityQueue<>();
        for (int n: nums) {
            pq.offer(n);
            if (pq.size() > k) {
                pq.poll();
            }
        }
        
    }
    
    public int add(int val) {
        this.pq.offer(val);
        if (this.pq.size() > this.k) {
            this.pq.poll();
        }
        return this.pq.peek();
    }
}
