class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bottomPrice = prices[0]
        maxP = 0
        for sell in prices:
            maxP = max(maxP, sell - bottomPrice)
            bottomPrice = min(sell, bottomPrice)
        return maxP