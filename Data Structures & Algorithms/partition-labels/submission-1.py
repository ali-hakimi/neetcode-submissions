class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        res = []
        start, end = 0, -1
        for i, c in enumerate(s):  
            end = max(end, lastIndex[c])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
                continue
        return res
