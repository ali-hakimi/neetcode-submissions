class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> res = new ArrayList<>();
        backtrack(new ArrayList<>(), 0, s, res);
        return res;
    }
    private void backtrack(List<String> sub, int idx, String s, List<List<String>> res) {
        if (idx == s.length()) {
            res.add(new ArrayList<>(sub));
        }
        for (int i = idx; i < s.length(); i++) {
            if (isPalindrome(s, idx, i)) {
                sub.add(s.substring(idx, i + 1));
                backtrack(sub, i + 1, s, res);
                sub.remove(sub.size() - 1);
            }
        }
    }

    private boolean isPalindrome(String s, int l, int r) {
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}
