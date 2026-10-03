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

public class Codec {
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null)
            return "";
        List<String> res = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty()) {
            int qSize = q.size();
            for (int i = 0; i < qSize; i++) {
                TreeNode node = q.poll();
                res.add(node == null ? "#" : node.val + "");
                if (node != null) {
                    q.offer(node.left);
                    q.offer(node.right);
                }
            }
        }
        // for (int i = res.size() - 1; i >= 0; i--) {
        //     if (!res.get(i).equals("#")) {
        //         break;
        //     }
        //     res.remove(i);
        // }
        return String.join(",", res);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.equals("")) {
            return null;
        }
        String[] nodes = data.split(",");
        int idx = 0;
        Queue<TreeNode> q = new LinkedList<>();
        TreeNode root = new TreeNode(Integer.parseInt(nodes[idx++]));
        q.offer(root);
        while (!q.isEmpty()) {
            int qSize = q.size();
            for (int i = 0; i < qSize; i++) {
                TreeNode node = q.poll();
                if (nodes[idx].equals("#")) {
                    node.left = null;
                } else {
                    node.left = new TreeNode(Integer.parseInt(nodes[idx]));
                    q.offer(node.left);
                }
                idx++;
                if (nodes[idx].equals("#")) {
                    node.right = null;
                } else {
                    node.right = new TreeNode(Integer.parseInt(nodes[idx]));
                    q.offer(node.right);
                }
                idx++;
            }
        }
        return root;
    }
}
