class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)

    def find(self, n1):
        while n1 != self.parent[n1]:
            self.parent[n1] = self.parent[self.parent[n1]]
            n1 = self.parent[n1]
        return n1

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        self.n -= 1
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

    def isConnected(self):
        return self.n == 1


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        N = len(edges)
        edges = [(u, v, w, i) for i, (u, v, w) in enumerate(edges)]
        edges.sort(key=lambda e: e[2])

        def findMST(idx, include):
            uf = UnionFind(n)
            minCost = 0

            if include:
                minCost += edges[idx][2]
                uf.union(edges[idx][0], edges[idx][1])

            for i, e in enumerate(edges):
                if i == idx:
                    continue
                if uf.union(e[0], e[1]):
                    minCost += e[2]

            return minCost if uf.isConnected() else -1

        minCost = findMST(0, True)
        critical, pseudo = list(), list()
        for i in range(N):
            cost = findMST(i, False)
            
            # If removing the edge increases cost or makes MST invalid
            if cost == -1 or cost > minCost:
                critical.append(edges[i][3])
                continue
            # Edge may be Pseudo
            cost = findMST(i, True)
            if cost == minCost:
                pseudo.append(edges[i][3])


        return [critical, pseudo]
