class FreqStack:

    def __init__(self):
        self.stack = {}
        self.maxCount = 0
        self.count = {}

    def push(self, val: int) -> None:
        valCount = 1 + self.count.get(val, 0)
        self.count[val] = valCount
        if valCount > self.maxCount:
            self.maxCount = valCount
            self.stack[valCount] = []
        self.stack[valCount].append(val)          
        
    def pop(self) -> int:
        val = self.stack[self.maxCount].pop()
        self.count[val] -= 1
        if len(self.stack[self.maxCount]) == 0:
            self.maxCount -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()