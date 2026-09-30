class Solution {
    public int mySqrt(int x) {
        int l = 0, r = x;
        int res = 0;
        while (l <= r) {
            int m = l + (r - l) / 2;
            long m2 = (long) m*m;
            if (m2 < x) {
                l = m + 1;
                res = m;
            } else if (m2 > x) {
                r = m - 1;
            }
            else {
                return m;
            }
        }
        return res;
    }
}