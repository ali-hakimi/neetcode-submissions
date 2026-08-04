class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalPost = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            jumpPower = nums[i]
            if jumpPower >= goalPost - i:
                goalPost = i
        return goalPost == 0