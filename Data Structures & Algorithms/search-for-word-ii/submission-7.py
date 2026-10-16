class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}

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
        res = []
        ROWS, COLS = len(board), len(board[0])

        def dfs(cur, i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS:
                return
            if board[i][j] not in cur.children:
                return
            char = board[i][j]
            cur = cur.children[char]
            if cur.word:
                res.append(cur.word)
                cur.word = None
            board[i][j] = "#"
            dfs(cur, i + 1, j)
            dfs(cur, i, j + 1)
            dfs(cur, i - 1, j)
            dfs(cur, i, j - 1)
            board[i][j] = char

        for i in range(ROWS):
            for j in range(COLS):
                dfs(root, i, j)
        return res
