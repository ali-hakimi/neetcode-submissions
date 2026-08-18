class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, pick):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    cur.append(nums[i])
                    pick[i] = True
                    dfs(cur, pick)
                    cur.pop()
                    pick[i] = False

        dfs([], [False] * len(nums))
        return res
