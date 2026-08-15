class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) == 0:
            return word2
        if len(word2) == 0:
            return word1

        a, b = 0, 0
        res = []
        while a < len(word1) and b < len(word2):
            if len(res) % 2 == 0:
                res.append(word1[a])
                a += 1
            else:
                res.append(word2[b])
                b += 1
        
        if a < len(word1):
            res.extend(c for c in word1[a:])
        if b < len(word2):
            res.extend(c for c in word2[b:])
        return "".join(res)
