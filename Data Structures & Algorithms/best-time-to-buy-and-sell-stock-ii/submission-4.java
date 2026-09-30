class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int buy = Integer.MAX_VALUE;

        for (int i = 0; i < prices.length; i++) {
            int prev = i == 0 ? Integer.MAX_VALUE : prices[i - 1];
            int next = i == prices.length - 1 ? Integer.MIN_VALUE : prices[i + 1];
            
            int cur = prices[i];
            if (cur < next && cur < buy) {
                buy = cur;
            } else if (cur > next && cur > buy) {
                profit += (cur - buy);
                buy = Integer.MAX_VALUE;
            }
        }

        return profit;
    }
}