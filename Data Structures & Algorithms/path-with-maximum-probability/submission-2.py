class Solution:
    def maxProbability( 
        self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int
    ) -> float:
        graph = defaultdict(list)
        for i, [a, b] in enumerate(edges):
            graph[a].append([succProb[i], b])
            graph[b].append([succProb[i], a])

        minHeap = [[-1, start_node]]
        nodeProb = {start_node: 1}
        while minHeap:
            prob1, a = heapq.heappop(minHeap)
            prob1 *= -1
            if a == end_node:
                return abs(prob1)
            for prob2, b in graph[a]:
                if b in nodeProb and nodeProb[b] >= prob2 * prob1:
                    continue
                nodeProb[b] = prob2 * prob1
                heapq.heappush(minHeap, [-nodeProb[b], b])
        return 0