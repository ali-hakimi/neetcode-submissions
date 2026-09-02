class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append([t, v])

        minHeap = [[0, k]]
        visitTime = {k: 0}

        while minHeap:
            t1, src = heapq.heappop(minHeap)

            for t2, dst in sorted(graph[src]):
                if dst in visitTime and visitTime[dst] <= t1 + t2:
                    continue
                visitTime[dst] = t1 + t2
                heapq.heappush(minHeap, [visitTime[dst], dst])
        return -1 if len(visitTime) < n else max(visitTime.values())