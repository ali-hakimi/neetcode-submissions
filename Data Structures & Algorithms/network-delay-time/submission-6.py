class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append([v, t])
        print(graph)
        visitTime = {k: 0}
        q = deque([[k, 0]])
        while q:
            u, t1 = q.popleft()
            print("11", u, t1)
            for v, t2 in graph[u]:
                print("13", t2, v)
                if v in visitTime and visitTime[v] <= (t1 + t2):
                        continue
                print("v:", v, "t1 + t2", t1 + t2)
                visitTime[v] = t1 + t2
                q.append([v, t1 + t2])
        print(visitTime)
        return -1 if len(visitTime) < n else max(visitTime.values()) if visitTime else -1