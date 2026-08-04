class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin = curMax = 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            elif n > 0:
                curMin, curMax = curMin * n, curMax * n
            else:
                curMin, curMax = min(curMax * n, n), max(curMin * n, n)
            res = max(res, curMax)
        return res

        10

        # n = -4 >> curMin = -4, curMax = -4
        # n = 1 >> curMin = -4, curMax = -4