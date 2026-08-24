class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}

        def dfs(i, m, alice):
            if i == len(piles):
                return 0
            if (i, m, alice) in dp:
                return dp[(i, m, alice)]

            res = 0 if alice else float("inf")
            total = 0
            for x in range(1, 2 * m + 1):
                if i + x > len(piles):
                    break
                total += piles[i + x - 1]
                if alice:
                    res = max(res, total + dfs(i + x, max(m, x), not alice))
                else:
                    res = min(res, dfs(i + x, max(m, x), not alice))
            dp[(i, m, alice)] = res
            return res
        return dfs(0, 1, True)