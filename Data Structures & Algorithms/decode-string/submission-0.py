class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur = ""
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append((cur, num))
                cur = ""
                num = 0
            elif c == "]":
                temp = cur
                cur, count = stack.pop()
                cur += temp * count
            else:
                cur += c
        return cur