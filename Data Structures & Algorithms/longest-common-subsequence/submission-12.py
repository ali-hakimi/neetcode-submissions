class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M = len(text1)
        N = len(text2)

        if min(M, N) == 0:
            return 0

        dp = [0] * (N + 1)

        for i in range(M - 1, -1, -1):
            prev = 0
            for j in range(N - 1, -1, -1):
                temp = dp[j]

                if text1[i] == text2[j]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j], dp[j + 1])
                prev = temp
        return dp[0]
