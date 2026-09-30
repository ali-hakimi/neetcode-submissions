class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String s : strs) {
            int len = s.length();
            sb.append(len);
            sb.append("#");
            sb.append(s);
        }
        
        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            int j = i;
            while (j < str.length() && str.charAt(j) != '#') {
                j += 1;
            }
            int len = Integer.parseInt(str.substring(i, j));
            String s = str.substring(j + 1, j + 1 + len);
            res.add(s);
            i = j + 1 + len;
        }

        return res;
    
    }
}
