class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}

        def dfs(i):
            if i == len(stoneValue):
                return 0
            if i in dp:
                return dp[i]

            res = float("-inf")
            for j in range(i, min(i + 3, len(stoneValue))):
                res = max(res, sum(stoneValue[i : j + 1])- dfs(j + 1)) 
            dp[i] = res
            return res

        if dfs(0) == 0:
            return "Tie"
        elif dfs(0) > 0:
            return "Alice"
        else:
            return "Bob"
