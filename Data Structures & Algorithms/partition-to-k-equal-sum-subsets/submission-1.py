class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        subsets = [0] * k
        nums.sort(reverse=True)

        def dfs(i):
            if i == len(nums):
                return True

            for j in range(k):
                if subsets[j] + nums[i] <= target:
                    subsets[j] += nums[i]
                    if dfs(i + 1):
                        return True
                    subsets[j] -= nums[i]
                
                if subsets[j] == 0:
                    break

            return False

        return dfs(0)
