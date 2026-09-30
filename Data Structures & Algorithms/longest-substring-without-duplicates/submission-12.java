class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l = 0, r = 0;
        int n = s.length();
        Set<Character> set = new HashSet<>();

        int res = 0;
        while (r < n) {
            while (set.contains(s.charAt(r))) {
                set.remove(s.charAt(l));
                l++;
            }
            set.add(s.charAt(r));
            r++;
            res = Math.max(res, r - l);    
        }
        return res;
    }
}
