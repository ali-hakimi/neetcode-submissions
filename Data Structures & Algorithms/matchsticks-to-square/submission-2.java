class Solution {
    public boolean makesquare(int[] matchsticks) {
        int sum = Arrays.stream(matchsticks).sum();
        if (sum % 4 != 0 || matchsticks.length < 4) {
            return false;
        }
        Arrays.sort(matchsticks);
        int[] sides = new int[4];
        int length = sum / 4;
        return dfs(matchsticks, sides, matchsticks.length, length);
    }
    private boolean dfs(int[] matchsticks, int[] sides, int index, int length) {
        if (index == 0) {
            return true;
        }
        for (int i = 0; i < 4; i++) {
            if (sides[i] + matchsticks[index - 1] <= length) {
                sides[i] += matchsticks[index - 1];
                if (dfs(matchsticks, sides, index - 1, length))
                    return true;
                sides[i] -= matchsticks[index - 1];
            }

            if (sides[i] == 0)
                break;
        }
        return false;
    }
}
