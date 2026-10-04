class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List < List<Integer>> perms = new ArrayList<>();
        List<Integer> sub = new ArrayList<>();
        perms.add(sub);

        for (int n : nums) {
            List<List<Integer>> newPerms = new ArrayList<>();
            for (List<Integer> p : perms) {
                for (int i = 0; i <= p.size(); i++) {
                    List<Integer> pCopy = new ArrayList<>(p);
                    pCopy.add(i, n);
                    newPerms.add(pCopy);
                }
            }
            perms = newPerms;
        }
        return perms;
    }
}
