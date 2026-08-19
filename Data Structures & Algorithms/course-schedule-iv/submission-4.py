class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[crs].append(pre)

        def dfs(crs):
            if crs not in preMap:
                preMap[crs] = set()
                for nei in adj[crs]:
                    preMap[crs] |= dfs(nei)
                preMap[crs].add(crs)
            return preMap[crs]
        preMap = {}
        for crs in range(numCourses):
            dfs(crs)


        res = []
        for u, v in queries:
            if u in preMap[v]:
                res.append(True)
            else:
                res.append(False)
        return res