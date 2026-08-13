class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]

        for sell in prices:
            profit = sell - buy
            if profit < 0:
                buy = sell
            else:
                res = max(res, profit)
        return res