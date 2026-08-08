class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}

        def dfs(i, j, k):
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            if (i, j) in dp:
                return dp[(i, j)]

            res = False
            if i < len(s1) and s3[k] == s1[i]:
                res = dfs(i + 1, j, k + 1)
            if j < len(s2) and s3[i + j] == s2[j]:
                res = dfs(i, j + 1, k + 1)
            dp[(i, j)] = res
            return res

        return dfs(0, 0, 0)
