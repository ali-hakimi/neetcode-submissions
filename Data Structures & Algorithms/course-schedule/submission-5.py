class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(set)
        for crs, pre in prerequisites:
            adj[crs].add(pre)
        
        visited, visiting = set(), set()

        def dfs(crs):
            if crs in visited:
                return True
            if crs in visiting:
                return False
            visiting.add(crs)
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True