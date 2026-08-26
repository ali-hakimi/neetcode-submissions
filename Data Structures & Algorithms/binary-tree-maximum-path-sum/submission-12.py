# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = float("-inf")
        def dfs(node):
            if not node:
                return 0

            leftPath = max(dfs(node.left), 0)
            rightPath = max(dfs(node.right), 0)

            path = leftPath + node.val + rightPath
            self.maxPath = max(self.maxPath, path)
            return max(node.val + leftPath, node.val + rightPath, 0)

        dfs(root)
        return self.maxPath
