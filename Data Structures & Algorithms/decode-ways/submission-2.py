class Solution:
    def numDecodings(self, s: str) -> int:
        one, two = 1, 0
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                print(i, dp[i])
                if (i + 2) < len(dp) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                    print("here")
                    dp[i] += dp[i + 2]
                    print("(i + 2)", i + 2)
                    print("len(dp)", len(dp))
                    print("dp[i + 2]", dp[i + 2])

        return dp[0]