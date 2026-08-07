class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        listSum = sum(nums)
        if listSum % 2:
            return False
        target = listSum // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for num in dp:
                if nums[i] + num == target:
                    return True
                nextDP.add(nums[i] + num)
                nextDP.add(num)
            dp = nextDP
        return False