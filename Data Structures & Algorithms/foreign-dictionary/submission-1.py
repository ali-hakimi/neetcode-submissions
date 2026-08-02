class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c: set() for w in words for c in w }

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        res = []
        visited, visiting = set(), set()

        def dfs(node):
            if node in visited:
                return True
            if node in visiting:
                return False
            
            visiting.add(node)
            print("node:", node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False

            visiting.remove(node)
            visited.add(node)
            res.append(node)
            print(res)
            return True
        for c in adj:
            if not dfs(c):
                return ""
        
        return "".join(res[::-1])

