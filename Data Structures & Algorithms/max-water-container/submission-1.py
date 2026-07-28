class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l , r = 0, len(heights) - 1

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            res = max(res, width * height)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return res
        