class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int n1 = s1.length(), n2 = s2.length();
        if (n1 > n2) {
            return false;
        }

        int[] map1 = new int[26];
        int[] map2 = new int[26];

        for (int i = 0; i < n1; i++) {
            map1[s1.charAt(i) - 'a']++;
            map2[s2.charAt(i) - 'a']++;
        }

        int matches = 0;
        for (int i = 0; i < 26; i++) {
            if (map1[i] == map2[i]) {
                matches++;
            }
        }

        int l = 0, r = n1;
        while (r < n2) {
            if (matches == 26) {
                return true;
            }

            map2[s2.charAt(l) - 'a']--;

            if (map1[s2.charAt(l) - 'a'] == map2[s2.charAt(l) - 'a']) {
                matches++;
            } else if (map1[s2.charAt(l) - 'a'] == map2[s2.charAt(l) - 'a'] + 1) {
                matches--;
            }

            map2[s2.charAt(r) - 'a']++;
            if (map1[s2.charAt(r) - 'a'] == map2[s2.charAt(r) - 'a']) {
                matches++;
            } else if (map1[s2.charAt(r) - 'a'] == map2[s2.charAt(r) - 'a'] - 1) {
                matches--;
            }
            l++;
            r++;
        }
        return matches == 26;
    }
}
