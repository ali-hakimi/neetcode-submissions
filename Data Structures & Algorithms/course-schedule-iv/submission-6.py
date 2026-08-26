class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, pre: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        adj = defaultdict(list)
        for a, b in pre:
            adj[a].append(b)

        graph = defaultdict(set)

        def dfs(src):
            if src in graph:
                return graph[src]
            for nei in adj[src]:
                graph[src].add(nei)
                graph[src] |= dfs(nei)
            return graph[src]

        for n in range(numCourses):
            dfs(n)

        res = []
        for a, b in queries:
            if a in graph and b in graph[a]:
                res.append(True)
            else:
                res.append(False)
        return res
