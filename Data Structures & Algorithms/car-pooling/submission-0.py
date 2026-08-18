class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])

        minHeap = []
        carPass = 0

        for numPass, start, end in trips:
            while minHeap and minHeap[0][0] <= start:
                carPass -= heapq.heappop(minHeap)[1]

            carPass += numPass
            if carPass > capacity:
                return False
            heapq.heappush(minHeap, [end, numPass])
        return True