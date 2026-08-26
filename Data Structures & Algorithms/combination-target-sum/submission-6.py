class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target:
                return 
            for i in range(idx, len(nums)):
                cur.append(nums[i])
                dfs(i, cur, total + nums[i])
                cur.pop()

        dfs(0, [], 0)
        return res
