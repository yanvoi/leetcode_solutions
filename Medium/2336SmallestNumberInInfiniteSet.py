class SmallestInfiniteSet:

    def __init__(self):
        self.heap = list(range(1, 1001))
        heapq.heapify(self.heap)
        self.not_popped = set(self.heap)

    def popSmallest(self) -> int:
        popped_value = heapq.heappop(self.heap)
        self.not_popped.remove(popped_value)
        return popped_value

    def addBack(self, num: int) -> None:
        if num not in self.not_popped:
            heapq.heappush(self.heap, num)
        
        self.not_popped.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
