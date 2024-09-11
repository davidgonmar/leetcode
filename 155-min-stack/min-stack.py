class MinStack:

    def __init__(self):
        self.data = []
        self.min = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if len(self.data) == 1:
            self.min.append(val)
        else:
            lastMin = self.min[-1]
            if val < lastMin:
                self.min.append(val)
            else:
                self.min.append(self.min[-1])
    def pop(self) -> None:
        self.data.pop(-1)
        self.min.pop(-1)

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()