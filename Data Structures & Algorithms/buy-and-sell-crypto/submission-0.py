class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bottom = prices[0]
        maxP = 0
        
        for sell in prices:
            maxP = max(maxP, sell - bottom)
            bottom = min(bottom, sell)
        return maxP