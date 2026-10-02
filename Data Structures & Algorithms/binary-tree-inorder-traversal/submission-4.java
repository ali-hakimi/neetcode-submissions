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
    public List<Integer> inorderTraversal(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();
        if (root.left != null) {
            left = inorderTraversal(root.left);
        }
        if (root.right != null) {
            right = inorderTraversal(root.right);
        }

        left.add(root.val);
        left.addAll(right);
        return left;   
    }
}