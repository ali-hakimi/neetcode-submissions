class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        cycle = 0

        while maxHeap or q:
            cycle += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, cycle + n])
            if q and q[0][1] == cycle:
                cnt = q.popleft()[0]
                if cnt:
                    heapq.heappush(maxHeap, cnt)
        return cycle
