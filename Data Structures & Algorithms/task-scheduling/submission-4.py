class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        cycle = 0
        q = deque()

        while maxHeap or q:
            cycle += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cycle + n, cnt])
            if q and q[0][0] == cycle:
                c, cnt = q.popleft()
                heapq.heappush(maxHeap, cnt)
        return cycle
                
                    
        