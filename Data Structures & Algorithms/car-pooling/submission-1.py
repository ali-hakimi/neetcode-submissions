class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])

        passengers = 0
        minHeap = []
        for n, start, end in trips:
            while minHeap and start >= minHeap[0][0]:
                passengers -= heapq.heappop(minHeap)[1]
            passengers += n
            if passengers > capacity:
                return False
            heapq.heappush(minHeap, [end, n])
            
        return True