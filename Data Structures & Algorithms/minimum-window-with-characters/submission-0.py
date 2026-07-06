class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        minLength = len(s) + 1
        ans = ""

        tCount, window = {}, {}

        for i in range(len(t)):
            tCount[t[i]] = 1 + tCount.get(t[i], 0)
        
        have, need = 0, len(tCount)
        l = 0
        for r in range(len(s)):           
            if s[r] in tCount:
                window[s[r]] = 1 + window.get(s[r], 0)
                if window[s[r]] == tCount[s[r]]:
                    have += 1

                while have == need:
                    if minLength > r - l + 1:
                        minLength = r - l + 1
                        ans = s[l:r+1]

                    if s[l] in tCount:
                        window[s[l]] -= 1
                        if window[s[l]] + 1 == tCount[s[l]]:
                            have -= 1
                    l += 1
                print(window)

        return ans