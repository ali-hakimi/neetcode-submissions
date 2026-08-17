class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            sub = 1
            cur = largest
            for n in nums:
                if cur - n < 0:
                    sub += 1
                    cur = largest
                    if sub > k:
                        return False
                cur -= n
            return sub <= k

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            m = (l + r) // 2
            if canSplit(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res
