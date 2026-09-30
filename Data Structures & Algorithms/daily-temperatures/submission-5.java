class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        Stack<int[]> st = new Stack<>();
        int[] output = new int[n];

        for (int i = 0; i < n; i++) {
            int cur = temperatures[i];
            while (!st.isEmpty() && st.peek()[0] < cur) {
                int[] pair = st.pop();
                output[pair[1]] = i - pair[1];
            }
            st.push(new int[] {cur, i});
        }
        return output;
    }
}
