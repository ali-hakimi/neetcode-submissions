class TreiNode:
    def __init__(self):
        self.word = False
        self.children = {}


class WordDictionary:
    def __init__(self):
        self.root = TreiNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreiNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(cur, i):
            if i == len(word):
                return cur.word
            if word[i] in cur.children:
                return dfs(cur.children[word[i]], i + 1)

            if word[i] == ".":
                for child in cur.children.values():
                    if dfs(child, i + 1):
                        return True
            return False

        return dfs(self.root, 0)
