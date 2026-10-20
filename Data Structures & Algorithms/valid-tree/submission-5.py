class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        visited, visiting = set(), set()

        def dfs(prev, node):
            if node in visited:
                return True
            if node in visiting:
                return False
            visiting.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(node, nei):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True
        return dfs(-1, 0) and len(visited) == n