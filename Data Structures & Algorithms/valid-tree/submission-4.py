class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(n)}
        for u, v in edges:
            preMap[u].append(v)
            preMap[v].append(u)

        visiting, visited = set(), set()

        def dfs(node, prev):
            if node in visited:
                return True
            if node in visiting:
                return False

            visiting.add(node)
            for nei in preMap[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True
        
        
        if not dfs(0, -1):
            return False
        return len(visited) == n 