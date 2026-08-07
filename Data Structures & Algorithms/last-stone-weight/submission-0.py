class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-s for s in stones] 
        heapq.heapify(minHeap)

        while len(minHeap) > 1:
            a, b = -heapq.heappop(minHeap), -heapq.heappop(minHeap)
            if a == b:
                continue
            else:
                heapq.heappush(minHeap, -abs(a - b))
        return -minHeap[0] if len(minHeap) else 0