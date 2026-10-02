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
    public int maxDepth(TreeNode root) {
        int depth = 0;
        Queue<TreeNode> q = new LinkedList<>();
        if (root != null)
            q.offer(root);
        while (!q.isEmpty()) {
            int qLen = q.size();
            for (int i = 0; i < qLen; i++) {
                TreeNode n2 = q.poll();
                if (n2.left != null)
                    q.offer(n2.left);
                if (n2.right != null)
                    q.offer(n2.right);
            }
            depth++;
        }
        return depth;
    }
}
