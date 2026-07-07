class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack = []
        output = [0] * len(t)

        for i in range(len(t)):
            while stack and stack[-1][0] < t[i]:
                temp, idx = stack.pop()
                output[idx] = i - idx
            stack.append([t[i], i])
            
        return output

                


        