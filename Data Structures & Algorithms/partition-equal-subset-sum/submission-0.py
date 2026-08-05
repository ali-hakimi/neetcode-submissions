class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2

        if target % 1:
            return False
        
        sums = set()

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            tmp = set()
            for s in sums:
                tmp.add(s + num)
            sums.add(num)
            sums.update(tmp)
            if target in sums:
                return True
        return False