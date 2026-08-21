class Solution:
    def maxProbability(
        self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int
    ) -> float:
        adj = defaultdict(list)
        for i, edge in enumerate(edges):
            src, dst = edge
            adj[src].append([dst, succProb[i]])
            adj[dst].append([src, succProb[i]])

        minHeap = [[-1, start_node]]
        visit = set()
        while minHeap:
            prob1, src = heapq.heappop(minHeap)
            if src == end_node:
                return -prob1
            visit.add(src)
            for dst, prob2 in adj[src]:
                if dst in visit:
                    continue
                heapq.heappush(minHeap, [prob1 * prob2, dst])

        return 0
