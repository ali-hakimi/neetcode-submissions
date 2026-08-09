class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) in cache:
                return cache[(i, j)]
            if word1[i] == word2[j]:
                cache[(i,j)] = dfs(i + 1, j + 1)
            else:
                delete = dfs(i + 1, j)
                replace = dfs(i + 1, j + 1)
                insert = dfs(i, j + 1)
                cache[(i,j)] = 1 + min(delete, replace, insert)
            return cache[(i,j)]

        return dfs(0,0)