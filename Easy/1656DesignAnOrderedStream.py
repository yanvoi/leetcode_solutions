class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.head = 1
        self.stream = [None] * (n + 1)

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        answer = []
        while self.head <= self.n and self.stream[self.head]:
            answer.append(self.stream[self.head])
            self.head += 1

        return answer

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
