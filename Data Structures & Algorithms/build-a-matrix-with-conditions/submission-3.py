class Solution:
    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:
        def fillAdj(conditions):
            adj = {}
            for a, b in conditions:
                if a not in adj:
                    adj[a] = set()
                adj[a].add(b)
            return adj

        def dfs(adj):
            nonlocal k
            visited, visiting = set(), set()
            res = []

            def dfs(i):
                if i in visited:
                    return True
                if i in visiting:
                    return False
                visiting.add(i)
                for nei in adj.get(i, []):
                    if not dfs(nei):
                        return False
                visiting.pop()
                visited.add(i)
                res.append(i)
                return True

            for i in range(1, k + 1):
                if not dfs(i):
                    return []
            return res[::-1]

        rowAdj, colAdj = fillAdj(rowConditions), fillAdj(colConditions)
        rows, cols = dfs(rowAdj), dfs(colAdj)

        if not rows or not cols:
            return []

        def helper(arr):
            mp = {}
            for i, val in enumerate(arr):
                mp[val] = i
            return mp

        rowMap, colMap = helper(rows), helper(cols)
        matrix = []
        j = 0
        for i in range(k):
            row = [0] * k
            matrix.append(row)

        for i in range(1, k + 1):
            if i in rowMap and i in colMap:
                matrix[rowMap[i]][colMap[i]] = i

        return matrix
