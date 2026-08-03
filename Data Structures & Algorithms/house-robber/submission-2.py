class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        one, two = nums[0], max(nums[1], nums[0])

        for i in range(2, len(nums)):
            ith = max(one + nums[i], two)
            one = two
            two = ith
        return two
