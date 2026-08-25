# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0
        stack = [(0, root)]
        while stack:
            depth, node = stack.pop()
            maxDepth = max(maxDepth, depth)
            if not node:
                continue
            stack.append((depth + 1, node.left))
            stack.append((depth + 1, node.right))
        return maxDepth