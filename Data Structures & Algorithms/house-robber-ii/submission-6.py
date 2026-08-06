class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robSub(nums[:len(nums)-1]),self.robSub(nums[1:]))
    
    def robSub(self, nums):
        one, two = 0, 0
        for i in range(len(nums) - 1, -1 ,-1):
            one, two = max(one, nums[i] + two), one
        return one