class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]

        for sell in prices:
            res = max(res, sell - buy)
            buy = min(buy, sell)
        return res