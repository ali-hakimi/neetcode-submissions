class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(cur, i):
            res.append(cur.copy())
            if len(cur) == len(nums):
                return
                
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                cur.append(nums[j])
                dfs(cur, j + 1)
                cur.pop()

        dfs([], 0)
        return res
