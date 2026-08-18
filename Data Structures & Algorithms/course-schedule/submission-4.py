class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited, visiting = set(), set()

        def dfs(i):
            if i in visited:
                return True
            if i in visiting:
                return False
            visiting.add(i)
            for pre in preMap[i]:
                if not dfs(pre):
                    return False
            visiting.remove(i)
            visited.add(i)
            return True

        for crs in preMap:
            if not dfs(crs):
                return False

        return True
