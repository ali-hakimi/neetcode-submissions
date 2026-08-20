class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append([v, t])
        visitTime = {k: 0}
        minHeap = [[0, k]]
        while minHeap:
            t1, u = heapq.heappop(minHeap)
            if t1 > visitTime[u]:
                continue
            for v, t2 in graph[u]:
                if v in visitTime and visitTime[v] <= (t1 + t2):
                    continue
                visitTime[v] = t1 + t2
                heapq.heappush(minHeap, [t1 + t2, v])
        return -1 if len(visitTime) < n else max(visitTime.values()) if visitTime else -1
