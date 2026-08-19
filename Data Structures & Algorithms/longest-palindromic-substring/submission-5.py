class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            for j in range(2):
                l, r = i, i + j
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l-=1
                    r+=1
                l+=1
                r-=1
                newLen = r - l + 1
                if newLen > resLen:
                    resLen = newLen
                    res = s[l: r + 1]

        return res