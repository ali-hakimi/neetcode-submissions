class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [0] * N
        for i in range(N):
            dp[i] = 0 if obstacleGrid[0][i] else 1
            if i > 0 and dp[i - 1] == 0:
                dp[i] = 0

        for i in range(1, M):
            for j in range(N):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]

        return dp[N - 1]
