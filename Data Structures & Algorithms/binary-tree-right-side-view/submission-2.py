# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)
        while q:
            lenQ = len(q)
            rightMost = None
            for _ in range(lenQ):
                node = q.popleft()
                if not node:
                    continue
                rightMost = node.val
                q.append(node.left)
                q.append(node.right)
            if rightMost:
                res.append(rightMost)
        return res