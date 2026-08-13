class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for n in numSet:
            if n - 1 in numSet:
                continue
            count = 1
            while n + 1 in numSet:
                count += 1
                n += 1
            res = max(res, count)
        return res
