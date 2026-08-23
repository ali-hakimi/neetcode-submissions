class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for i in range(1, m):
            col = 0
            for j in range(n):
                dp[j] += col
                col = dp[j]
        return dp[n - 1]
