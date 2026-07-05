class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l, r = 0, 0

        while r < len(s):
            while s[r] in s[l:r]:
                l += 1
            longest = max(longest, r - l + 1)
            r += 1

        return longest