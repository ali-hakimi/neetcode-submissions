# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        preorder = []
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                preorder.append(str(curr.val))
                curr = curr.left
            preorder.append("N")
            curr = stack.pop()
            curr = curr.right

        preorder.append("N")
        return ",".join(preorder)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0
        print(vals)
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
       


