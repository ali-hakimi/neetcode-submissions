class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] countS = new int[26];
        int[] countT = new int[26];

        for (char c : s.toCharArray()) {
            int idx = (int) (c - 'a');
            countS[idx]++;
        }
        for (char c : t.toCharArray()) {
            int idx = (int) (c - 'a');
            countT[idx]++;
        }
        for (int i = 0; i < 26; i++) {
            if (countS[i] != countT[i]){
                return false;
            }
        }
        return true;
    }
}
