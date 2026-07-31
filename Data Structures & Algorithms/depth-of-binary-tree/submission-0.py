# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        stack = [(1, root)]
        while stack:
            depth, node = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.extend([(depth + 1, node.left), (depth + 1, node.right)])
        return max_depth
        