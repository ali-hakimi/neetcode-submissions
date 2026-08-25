class Solution:
    def isValid(self, s: str) -> bool:
        mp = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if stack and c in mp:
                if stack[-1] != mp[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
