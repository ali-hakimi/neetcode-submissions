class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 1) {
            return strs[0];
        }
        String res = strs[0]; 
        for (int i = 1; i < strs.length; i++) {
            int minLen = Math.min(res.length(), strs[i].length());
            int j = 0;
            while (j < minLen && res.charAt(j) == strs[i].charAt(j)) {
                j++;
            }
            res = res.substring(0, j);
            if (res.isEmpty()) { 
                return res;
            }
        }
        return res;
    }
}