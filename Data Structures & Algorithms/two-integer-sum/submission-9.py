class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in pre:
                return [pre[diff], i]
            pre[nums[i]] = i
        