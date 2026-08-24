class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        minHeap = []
        for n, v in count.items():
            minHeap.append((-v, n))
        
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            print(k)
            res.append(heapq.heappop(minHeap)[1])
            k-=1
        return res