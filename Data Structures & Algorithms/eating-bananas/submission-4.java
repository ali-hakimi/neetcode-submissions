class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int max = 0;
        for (int p: piles) {
            max = Math.max(max, p);
        }

        int l = 1, r = max;
        int res = r;
        while (l <= r) {
            int m = l + (r - l) / 2;
            int hrs = 0;
            for (int p: piles) {
                hrs += Math.ceil((double) p / m);
            }

            if (hrs <= h) {
                res = m;
                r = m - 1;
            }
            else {
                l = m + 1;
            }
        }
        return res;
    }
}
