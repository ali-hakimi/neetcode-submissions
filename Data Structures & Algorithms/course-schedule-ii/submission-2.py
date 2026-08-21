class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        visited, visiting, res = set(), set(), []
        def dfs(src):
            if src in visited:
                return True
            if src in visiting:
                return False
            visiting.add(src)
            for nei in adj[src]:
                if not dfs(nei):
                    return False
            res.append(src)
            visiting.remove(src)
            visited.add(src)
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return []
        return res