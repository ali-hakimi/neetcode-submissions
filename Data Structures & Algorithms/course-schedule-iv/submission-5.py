class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        graph = defaultdict(set)

        def dfs(src):
            if src not in graph:
                graph[src] = set()
                for nei in adj[src]:
                    graph[src].add(nei)
                    graph[src] |= dfs(nei)
            return graph[src]

        for n in range(numCourses):
            dfs(n)

        print(graph)
        res = []
        for u, v in queries:
            res.append(v in graph[u])
        return res
