class MinStack:

    def __init__(self):
        self.arr = []
        self.min = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.min:
            self.min.append(val)
        elif val < self.min[-1]:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])

    def pop(self) -> None:
        self.arr.pop()
        self.min.pop()

    def top(self) -> int:
        return self.arr[-1] if len(self.arr) >= 1 else 'The Stack is Empty'

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
