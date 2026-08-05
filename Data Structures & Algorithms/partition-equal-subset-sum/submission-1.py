class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums % 2:
            return False

        dp = set()
        dp.add(0)
        target = sums // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if nums[i] + t == target:
                    return True
                nextDP.add(nums[i] + t)
                nextDP.add(t)
            dp = nextDP
        return False