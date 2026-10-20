class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: set() for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].add(pre)
        
        res = []
        visiting, visited = set(), set()

        def dfs(crs):
            if crs in visited:
                return True
            if crs in visiting:
                return False
            visiting.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False;
            res.append(crs)
            visiting.remove(crs)
            visited.add(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res