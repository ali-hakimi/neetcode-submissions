class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        res = 0
        
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                if maxLeft - height[l] > 0:
                    res += maxLeft - height[l]
            else:
                r-= 1
                maxRight = max(maxRight, height[r])
                if maxRight - height[r] > 0:
                    res += maxRight - height[r]
        return res