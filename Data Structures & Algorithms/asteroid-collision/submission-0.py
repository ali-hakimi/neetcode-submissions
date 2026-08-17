class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                prev = stack.pop()
                if abs(prev) == abs(a):
                    a=0
                    break
                elif abs(prev) > abs(a):
                    stack.append(prev)
                    a=0
                    break
                else:
                    continue
            if a:
                stack.append(a)
        return stack
