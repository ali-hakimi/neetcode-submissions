class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        if not len(nums):
            return 0
        if len(nums) < 2:
            return nums[0]

        first, second = nums[0], max(nums[1], nums[0])

        for i in range(2, len(nums)):
            ith = max(second, first + nums[i])
            first = second
            second = ith
        return second