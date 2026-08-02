class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visiting = set()
        def dfs(node, prev):
            if node in visiting:
                return False

            visiting.add(node)
            for v in adj[node]:
                if v == prev:
                    continue
                if not dfs(v, node):
                    return False
            return True

        return dfs(0, -1) and len(visiting) == n 
