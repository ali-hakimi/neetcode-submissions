class Solution {
    public int maxProfit(int[] prices) {
        int buy = prices[0];
        int max = 0;
        for (int sell: prices) {
            if (sell < buy) {
                buy = sell;
            }
            max = Math.max(max, sell - buy);
        }
        return max;
    }
}
