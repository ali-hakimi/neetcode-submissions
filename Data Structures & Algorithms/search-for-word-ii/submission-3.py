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

        def dfs(r, c, cur):
            if not (0 <= r < ROWS) or not (0 <= c < COLS):
                return
            if board[r][c] == "#" or board[r][c] not in cur.children:
                return

            ch = board[r][c]
            cur = cur.children[ch]
            
            if cur.word:
                res.append(cur.word)
                cur.word = None
                
            board[r][c] = "#"
            dfs(r + 1, c, cur)
            dfs(r - 1, c, cur)
            dfs(r, c + 1, cur)
            dfs(r, c - 1, cur)
            board[r][c] = ch


        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, root)

        return res
         