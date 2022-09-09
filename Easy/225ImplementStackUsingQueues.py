class MyStack:

    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        
        if not self.q1: return
        
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
            
        to_pop = self.q1.popleft()
        self.q1 = self.q2.copy()
        self.q2.clear()
        
        return to_pop

    def top(self) -> int:
        
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
            
        to_top = self.q1[0]
        self.q2.append(self.q1.popleft())
        
        self.q1 = self.q2.copy()
        self.q2.clear()
        
        return to_top

    def empty(self) -> bool:
        return not self.q1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
