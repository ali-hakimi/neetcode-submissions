class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i + 1 :[] for i in range(n)}
        for u, v, t in times:
            adj[u].append([v, t])

        visited = set()
        minHeap = [[0, k]]
        while minHeap:
            t1, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return t1
            for nei, t2 in adj[node]:
                heapq.heappush(minHeap, [t1 + t2, nei])
        return -1