class Solution {
    public int maxArea(int[] heights) {
        int n = heights.length;
        int l = 0, r = n - 1;
        int res = 0;

        while (l < r) {
            int width = r - l;
            int h = Math.min(heights[l], heights[r]);
            int area = width * h;
            res = Math.max(res, area);

            if (heights[l] < heights[r]) {
                l++;
            } else {
                r--;
            }
        }
        return res;
    }
}
