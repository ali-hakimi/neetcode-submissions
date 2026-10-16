class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                print("here")
                return False
            
            for j in range(minLen):
                if mp[w1[j]] > mp[w2[j]]:
                    print(w1, w2)
                    return False
                if mp[w1[j]] < mp[w2[j]]:
                    break
        return True