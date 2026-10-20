class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        for u, v in prerequisites:
            adj[u].append(v)

        visited, visiting = set(), set()

        def dfs(crs):
            if crs in visited:
                return True
            if crs in visiting:
                return False

            visiting.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
