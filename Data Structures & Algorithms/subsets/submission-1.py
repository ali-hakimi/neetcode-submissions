class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, cur):
            res.append(cur.copy())
            
            for j in range(i, len(nums)):
                cur.append(nums[j])
                dfs(j + 1, cur)
                cur.pop()

    
        dfs(0, [])
        return res