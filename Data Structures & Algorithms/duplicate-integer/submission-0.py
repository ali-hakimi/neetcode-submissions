class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set1 = set(nums)

        return len(nums) != len(set1)