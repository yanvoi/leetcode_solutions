class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [-1] * (k + 1)
        self.tail = 0
        self.next_place = 0
        self.length = k
        

    def enQueue(self, value: int) -> bool:
        
        if self.isFull():
            return False
        
        self.q[self.next_place] = value
        self.next_place = (self.next_place + 1) % (self.length + 1)
        
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.q[self.tail] = -1
        self.tail = (self.tail + 1) % (self.length + 1)
        
        return True

    def Front(self) -> int:
        
        if self.isEmpty():
            return -1
        
        return self.q[self.tail]
        

    def Rear(self) -> int:
        
        if self.isEmpty():
            return -1
        
        return self.q[self.next_place-1]
        

    def isEmpty(self) -> bool:
        
        if self.next_place == self.tail:
            return True
        
        return False
    

    def isFull(self) -> bool:
        
        if self.tail == 0 and self.next_place == self.length:
            return True
        
        if self.tail - 1 == self.next_place:
            return True

        return False
        

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
