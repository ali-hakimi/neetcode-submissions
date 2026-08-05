class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        res = []
        visiting, visited = set(), set()

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True

            visiting.add(crs)
            for nei in preMap[crs]:
                if not dfs(nei):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res
