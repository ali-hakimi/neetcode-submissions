class MinStack:

    def __init__(self):
        self.stack = []
        self.minVals = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minVals:
            minVal = min(self.minVals[-1], val)
        else:
            minVal = val
        self.minVals.append(minVal)

        

    def pop(self) -> None:
        self.stack.pop()
        self.minVals.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVals[-1]

