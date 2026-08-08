class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = 0
            if s[i] == t[j]:
                res = dfs(i + 1, j + 1)
            res += dfs(i + 1, j)

            dp[(i, j)] = res
            return res                      

        return dfs(0, 0)