class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        adj = {i: set() for i in range(numCourses)}

        for a, b in prerequisites:
            adj[a].add(b)
        
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
            res.append(a in graph and b in graph[a])
        return res
            