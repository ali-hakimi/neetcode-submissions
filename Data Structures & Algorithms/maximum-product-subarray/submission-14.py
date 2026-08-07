class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            elif n > 0:
                curMin, curMax = curMin * n, curMax * n
            else:
                curMin, curMax = min(n, curMax * n), max(n, curMin * n)
            res = max(res, curMax)
        return res