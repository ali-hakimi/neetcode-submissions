class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = [[] for i in range(N)]

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):   
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([cost, j])
                adj[j].append([cost, i])
        
        minHeap = [[0, 0]]
        minCost = 0
        visit = set()
        while minHeap and len(visit) != N:
            cost, src = heapq.heappop(minHeap)
            if src in visit:
                continue
            visit.add(src)
            minCost += cost

            for neiCost, nei in adj[src]:
                if nei in visit:
                    continue
                heapq.heappush(minHeap, [neiCost, nei])
        return minCost
                
                
        