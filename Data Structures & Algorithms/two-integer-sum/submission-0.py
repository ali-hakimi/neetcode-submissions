class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in dict1:
                dict1[nums[i]] = i
            else:
                return [dict1[diff], i]
        return [-1,-1]
        