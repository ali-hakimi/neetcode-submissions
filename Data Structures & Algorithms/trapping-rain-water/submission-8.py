class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        while l <= r:
            if maxLeft < maxRight:
                if maxLeft > height[l]:
                    res += maxLeft - height[l]
                else:
                    maxLeft = height[l]
                l += 1
            else:
                if maxRight > height[r]:
                    res += (maxRight - height[r])
                else:
                    maxRight = height[r]
                r -= 1
        return res