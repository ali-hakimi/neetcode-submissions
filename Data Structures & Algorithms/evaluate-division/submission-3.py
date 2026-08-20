class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        adj = collections.defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1

            q = deque()
            q.append([src, 1])
            visit = set()
            while q:
                n, w = q.popleft()
                if n in visit:
                    continue
                visit.add(n)
                for n2, w2 in adj[n]:
                    if target == n2:
                        return w * w2
                    q.append([n2, w * w2])
            return -1

        res = []
        for q in queries:
            res.append(bfs(q[0], q[1]))
        return res
