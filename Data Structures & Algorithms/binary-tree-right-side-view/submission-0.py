# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSide = 0
        res = []
        if not root:
            return res

        q = deque([root])
        while q:
            lenQ = len(q)
            for _ in range(lenQ):
                node = q.popleft()
                rightSide = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(rightSide)
        return res
            
            
