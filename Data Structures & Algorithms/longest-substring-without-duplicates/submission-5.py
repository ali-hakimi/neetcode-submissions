class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSub = 0
        l, r = 0, 0
        sub = []
        while r < len(s):
            if s[r] not in sub:
                sub.append(s[r])
                r += 1
            else:
                longestSub = max(longestSub, len(sub))
                while s[r] in sub:
                    sub.pop(0)
        return max(longestSub, len(sub))
        