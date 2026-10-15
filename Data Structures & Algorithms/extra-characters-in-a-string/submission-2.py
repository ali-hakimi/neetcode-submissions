class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            cur = self.root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = Trie(dictionary).root
        dp = {len(s): 0}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            cur = root            
            res = 1 + dfs(i + 1)
            for j in range(i, len(s)):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.word:
                    res = min(res, dfs(j + 1))
            dp[i] = res
            return res

        return dfs(0)