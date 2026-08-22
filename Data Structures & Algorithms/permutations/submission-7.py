class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            if i == len(nums):
                return [[]]
            res = []
            perms = dfs(i + 1)
            for p in perms:
                for j in range(len(p) + 1):
                    copy = p.copy()
                    copy.insert(j, nums[i])
                    res.append(copy)
            return res
        return dfs(0)