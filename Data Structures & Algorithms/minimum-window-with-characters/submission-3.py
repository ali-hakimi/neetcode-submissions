class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0 or len(s) < len(t):
            return ""
        
        tCount, window = {}, {}

        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)
        
        have, need = 0, len(tCount)
        res, resLen = [-1,-1], float("infinity")

        l = 0
        for r in range(len(s)):
            c = s[r]

            if c in tCount:
                window[c] = 1 + window.get(c, 0)
                if window[c] == tCount[c]:
                    have += 1

            while have == need:
                #update result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                #shrink window
                if s[l] in tCount:
                    window[s[l]] -= 1
                    if window[s[l]] < tCount[s[l]]:
                        have -= 1
                l+=1
                
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""