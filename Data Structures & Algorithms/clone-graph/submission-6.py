"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mp = {None: None}

        def dfs(node):
            if node in mp:
                return mp[node]
            copy = Node(node.val)
            mp[node] = copy
            for nei in node.neighbors:
                neiCopy = dfs(nei)
                copy.neighbors.append(neiCopy)
            return copy
        
        return dfs(node) if node else None
