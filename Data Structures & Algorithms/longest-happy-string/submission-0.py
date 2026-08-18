class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        minHeap = []
        for count, char in [[a, "a"], [b, "b"], [c, "c"]]:
            if count:
                heapq.heappush(minHeap, [-count, char])

        res = []
        while minHeap:
            cnt, char = heapq.heappop(minHeap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not minHeap:
                    break
                cnt2, char2 = heapq.heappop(minHeap)
                res.append(char2)
                cnt2+=1
                if cnt2:
                    heapq.heappush(minHeap, [cnt2, char2])
                heapq.heappush(minHeap, [cnt, char])
            else:
                res.append(char)
                cnt+=1
                if cnt:
                    heapq.heappush(minHeap, [cnt, char])
        return "".join(res)