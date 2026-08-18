class Solution:
    def totalNQueens(self, n: int) -> int:
        col, row, postDiag, negDiag = set(), set(), set(), set()
        count = 0

        def backtrack(r):
            nonlocal count
            if r == n:
                count += 1
                return

            for c in range(n):
                if c in col or r in row or (r + c) in postDiag or (r - c) in negDiag:
                    continue
                col.add(c)
                row.add(r)
                postDiag.add(r + c)
                negDiag.add(r - c)
                backtrack(r + 1)
                col.remove(c)
                row.remove(r)
                postDiag.remove(r+c)
                negDiag.remove(r-c)
        backtrack(0)
        return count