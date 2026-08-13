class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1
        while l < r:
            width = r - l
            if heights[l] < heights[r]:
                res = max(res, heights[l] * width)
                l+=1
            else:
                res = max(res, heights[r] * width)
                r-=1
        return res
