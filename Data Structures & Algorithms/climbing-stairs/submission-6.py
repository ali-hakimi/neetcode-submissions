class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        one, two = 1, 2

        for i in range(3, n + 1):
            temp = one
            one = two
            two = temp + two
        return two