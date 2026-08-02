class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = word
    
    def addWords(self, words):
        for word in words:
            self.addWord(word)
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        root.addWords(words)

        ROWS, COLS = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            if not (0 <= r < ROWS) or not (0 <= c < COLS):
                return
            
            char = board[r][c]
            if char == "#" or char not in node.children:
                return
            
            node = node.children[char]
            if node.word:
                result.append(node.word)
                node.word = None

            board[r][c] = "#"
            dfs(r + 1, c, node)
            dfs(r, c + 1, node)
            dfs(r - 1, c, node)
            dfs(r, c - 1, node)
            board[r][c] = char

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, root)
        
        return result
