class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, cur):
            if len(cur) == k:
                res.append(cur.copy())
                return
            for j in range(i, n + 1):
                cur.append(j)
                dfs(j + 1, cur)
                cur.pop()
        dfs(1, [])
        return res