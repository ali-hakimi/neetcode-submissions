# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        q = deque()
        q.append((root, float("-inf")))
        while q:
            lenQ = len(q)
            for _ in range(lenQ):
                node, prevMax = q.popleft()
                if not node:
                    continue
                if node.val >= prevMax:
                    count += 1
                    prevMax = node.val
                q.append((node.left, prevMax))
                q.append((node.right, prevMax))
        return count