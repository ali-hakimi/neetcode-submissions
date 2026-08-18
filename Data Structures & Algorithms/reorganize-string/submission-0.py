class Solution:
    def reorganizeString(self, s: str) -> str:
        countMap = Counter(s)
        minHeap = [[-cnt, c] for c, cnt in countMap.items()]
        heapq.heapify(minHeap)
        
        prev = None
        res = ""
        while minHeap or prev:
            if prev and not minHeap:
                return ""
            
            cnt, c = heapq.heappop(minHeap)
            res += c
            cnt += 1

            if prev:
                heapq.heappush(minHeap, prev)
                prev = None
            
            if cnt:
                prev = [cnt, c]
        return res