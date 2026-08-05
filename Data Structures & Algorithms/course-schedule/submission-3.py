class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting, visited = set(), set()

        def dfs(crs):
            if crs in visited:
                return True
            if crs in visiting:
                return False

            visiting.add(crs)
            for nei in preMap[crs]:
                if not dfs(nei):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            return True

        for crs in preMap:
            if not dfs(crs):
                return False
        return True
