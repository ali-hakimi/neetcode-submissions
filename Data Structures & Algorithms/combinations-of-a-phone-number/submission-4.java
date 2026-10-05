class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> res = new ArrayList<>();
        if (digits.isEmpty()) {
            return res;
        }
        res.add("");
        String[] digitToChar = {"", "", "abc", "def", "ghi", "jkl", "mno", "qprs", "tuv", "wxyz"};
        for (char digit: digits.toCharArray()) {
            List<String> tmp = new ArrayList<>();
            for (String curStr : res) {
                for (char c : digitToChar[digit - '0'].toCharArray()) {
                    tmp.add(curStr + c);
                }
            }
            res = tmp;
        }
        return res;
    }
}
