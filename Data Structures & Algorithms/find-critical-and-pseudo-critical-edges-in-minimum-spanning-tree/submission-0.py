class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)

    def find(self, n1):
        res = n1
        while res != self.par[res]:
            self.par[res] = self.par[self.par[res]]
            res = self.par[res]
        return res

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = self.par[p1]
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = self.par[p2]
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        N = len(edges)
        for idx in range(len(edges)):
            edges[idx].append(idx)

        edges.sort(key=lambda e: e[2])
        critical, pseudoCritical = [], []
        minCost = 0
        forcedEdge = False
        k = -1
        while k < N:
            uf = UnionFind(n)
            minHeap = list(edges)
            poppedEdge = []
            if k != -1:
                poppedEdge = minHeap.pop(k)

            cost = 0
            edgeCount = 0
            if forcedEdge:
                uf.union(poppedEdge[0], poppedEdge[1])
                cost += poppedEdge[2]
                edgeCount += 1
            for u, v, w, idx in minHeap:
                if not uf.union(u, v):
                    continue
                cost += w
                edgeCount += 1

            if k == -1:
                minCost = cost
                k += 1
                continue

            if forcedEdge:
                forcedEdge = False
                if cost == minCost:
                    pseudoCritical.append(poppedEdge[3])

            elif cost > minCost or edgeCount < n - 1:
                critical.append(poppedEdge[3])
            else:
                forcedEdge = True
                continue

            k += 1
        return [critical, pseudoCritical]
