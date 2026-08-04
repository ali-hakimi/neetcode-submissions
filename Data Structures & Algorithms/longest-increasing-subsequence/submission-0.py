class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * (len(nums))
        lis = 0
        for i in range(len(nums) - 1, -1, -1):
            longest = 0
            for j in range(i + 1, len(dp)):
                if nums[i] < nums[j] and dp[j] > longest:
                    longest = dp[j]
            dp[i] = longest + 1
            lis = max(lis, dp[i])

        return lis