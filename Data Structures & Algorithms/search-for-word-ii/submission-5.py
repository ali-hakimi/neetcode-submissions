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
        res = []

        def dfs(node, r, c):
            if not (0 <= r < ROWS) or not (0 <= c < COLS):
                return
            if board[r][c] not in node.children:
                return

            char = board[r][c]
            node = node.children[char]
            
            if node.word:
                res.append(node.word)
                node.word = None

            board[r][c] = "#"
            dfs(node, r - 1, c)
            dfs(node, r + 1, c)
            dfs(node, r, c + 1)
            dfs(node, r, c - 1)
            board[r][c] = char
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(root, i, j)
        return res