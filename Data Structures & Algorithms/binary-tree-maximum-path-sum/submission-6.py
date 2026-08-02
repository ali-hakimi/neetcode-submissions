# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int: 
        res = float("-inf")

        def dfs(node):
            if not node:
                return 0
            
            maxLeft = max(0, dfs(node.left))
            maxRight = max(0, dfs(node.right))

            nonlocal res
            res = max(res, node.val + maxLeft + maxRight)
            return node.val + max(maxLeft, maxRight)
        dfs(root)

        return res
        