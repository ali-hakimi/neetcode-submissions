class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        edgeCount = {}
        leaves = deque()
        for src, neis in adj.items():
            if len(neis) == 1:
                leaves.append(src)
            edgeCount[src] = len(neis)

        while leaves:
            if n <= 2:
                return list(leaves)
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edgeCount[nei] -= 1
                    if edgeCount[nei] == 1:
                        leaves.append(nei)
