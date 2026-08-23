class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, n1):
        while n1 != self.par[n1]:
            self.par[n1] = self.par[self.par[n1]]
            n1 = self.par[n1]
        return n1

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        self.n -= 1
        if self.rank[p2] > self.rank[p1]:
            self.rank[p2] += self.rank[p1]
            self.par[p1] = p2
        else:
            self.rank[p1] += self.rank[p2]
            self.par[p2] = p1
        return True
    
    def isConnected(self):
        return self.n == 1


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))

        factor_index = {}
        for i, n in enumerate(nums):
            f = 2
            while f * f <= n:
                if n % f == 0:
                    if f in factor_index:
                        uf.union(i, factor_index[f])
                    else:
                        factor_index[f] = i
                    while n % f == 0:
                        n = n // f
                f += 1
            if n > 1:
                if n in factor_index:
                    uf.union(i, factor_index[n])
                else:
                    factor_index[n] = i
        return uf.isConnected() 





        print(commonDivisors)
        return False