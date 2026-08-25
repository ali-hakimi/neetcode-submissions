class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            count = 1
            curCap = 0
            for i in range(len(weights)):
                if curCap + weights[i] > cap:
                    count += 1
                    curCap = weights[i]
                    if count > days:
                        return False
                else:
                    curCap += weights[i]
            return count <= days

        while l <= r:
            m = (l + r) // 2
            if canShip(m):
                res = min(r, m)
                r = m - 1
            else:
                l = m + 1
            
        return res