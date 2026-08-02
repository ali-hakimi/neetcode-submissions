# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or len(preorder) == 0:
            return None
        if not inorder or len(inorder) == 0:
            return None

        rootVal = preorder[0]
        print(rootVal)
        root = TreeNode(rootVal)
        rootIdx = inorder.index(rootVal)
        root.left = self.buildTree(preorder[1:], inorder[: rootIdx])
        root.right = self.buildTree(preorder[1 + rootIdx:], inorder[rootIdx + 1:])
        return root