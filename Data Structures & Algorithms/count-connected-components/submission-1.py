class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
            return True

        count = 0
        for node in range(n):
            if dfs(node):
                count +=1       

        return count