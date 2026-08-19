class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        dp = {}

        for i in range(len(s)):
            for j in range(2):
                l, r = i, i + j
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l-= 1
                    r+= 1
                    count+=1
        return count