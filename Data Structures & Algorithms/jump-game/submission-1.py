class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalPost = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            jumpPower = nums[i]
            if goalPost - i <= jumpPower:
                goalPost = i
        return goalPost == 0