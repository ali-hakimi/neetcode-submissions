class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()   
        
        res = 0
        prevEnd = float("-inf")
        for start, end in intervals:
            if prevEnd <= start:
                prevEnd = end
            else:
                prevEnd = min(prevEnd, end)
                res += 1

        return res