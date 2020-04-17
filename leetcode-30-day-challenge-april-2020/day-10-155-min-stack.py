class MinStack:
    def __init__(self):
        self.stack = []
        self.min = 99999999999

    def push(self, x: int) -> None:
        self.stack.append((x,min(self.getMin(),x)))


    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]


    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return 9999999999




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
