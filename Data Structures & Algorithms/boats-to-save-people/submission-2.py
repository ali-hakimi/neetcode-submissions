class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        print(people )
        l, r = 0, len(people) - 1
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            res += 1
            r -= 1
        return res