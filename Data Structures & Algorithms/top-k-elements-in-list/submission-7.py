class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        minHeap = []
        for num, cnt in count.items():
            minHeap.append([-cnt, num])
        heapq.heapify(minHeap)

        res = []
        while k:
            res.append(heapq.heappop(minHeap)[1])
            k-=1
        return res