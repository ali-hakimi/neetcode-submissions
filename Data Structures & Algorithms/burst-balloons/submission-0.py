class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}

        def dfs(numList):
            if len(numList) == 1:
                return numList[0]
            if tuple(numList) in dp:
                return dp[tuple(numList)]
            res = 0

            for i in range(len(numList)):
                prev = numList[i - 1] if (i - 1) >= 0 else 1
                n = numList[i]
                nex = numList[i + 1] if (i + 1) < len(numList) else 1

                recurse = 0
                if i == 0:
                    recurse = dfs(numList[1:])
                elif i == len(numList) - 1:
                    recurse = dfs(numList[:-1])
                else :
                    recurse = dfs(numList[:i] + numList[i + 1:])
                
                res = max(res, prev * n * nex + recurse)

            dp[tuple(numList)] = res

            return res

        return dfs(nums)
