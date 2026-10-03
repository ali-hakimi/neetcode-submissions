/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int rob(TreeNode root) {
        int[] res = rob2(root);
        return Math.max(res[0], res[1]);
    }
    public int[] rob2(TreeNode root) {
        if (root == null) {
            return new int[] {0, 0};
        }
        int[] left = rob2(root.left);
        int[] right = rob2(root.right);
        int include = root.val + left[1] + right[1];
        int exclude = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        System.out.println(root.val + " " + include + " " + exclude);
        return new int[] {include, exclude};
    }
}