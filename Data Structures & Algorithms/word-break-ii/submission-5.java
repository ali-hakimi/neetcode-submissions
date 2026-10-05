class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        List<String> res = new ArrayList<>();
        List<String> cur = new ArrayList<>();
        backtrack(0, cur, s, wordDict, res);
        return res;
    }
    private void backtrack(
        int idx, List<String> cur, String s, List<String> wordDict, List<String> res) {
        if (idx == s.length()) {
            res.add(String.join(" ", cur));
            return;
        }
        for (int i = idx; i < s.length(); i++) {
            if (wordDict.contains(s.substring(idx, i + 1))) {
                cur.add(s.substring(idx, i + 1));
                backtrack(i + 1, cur, s, wordDict, res);
                cur.remove(cur.size() - 1);
            }
        }
    }
}