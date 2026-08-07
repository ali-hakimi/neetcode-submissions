class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n > 0:
                curMin *= n
                curMax *= n
            elif n < 0:
                curMin, curMax = min(n, curMax * n), max(n, curMin * n)
            else:
                curMin, curMax = 1, 1
                continue
            res = max(res, curMax)
        return res