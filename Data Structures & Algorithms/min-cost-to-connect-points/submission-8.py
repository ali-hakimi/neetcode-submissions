class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        graph = defaultdict(list)

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dst = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append([dst, j])
                graph[j].append([dst, i])
        visit = set()
        cost = 0
        minHeap = [[0, 0]]
        while minHeap and len(visit) != N:
            dst, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            cost += dst
            for dst2, node2 in graph[node]:
                if node2 in visit:
                    continue
                heapq.heappush(minHeap, [dst2, node2])
                       
        return cost
