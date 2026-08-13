class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n * 2

        for i, num in enumerate(nums):
            ans[i] = ans[i + n] = num
        return ans