import heapq


class MedianFinder:

    def __init__(self):
        self.smaller = []
        self.bigger = []

    def addNum(self, num: int) -> None:
        if len(self.smaller) == len(self.bigger):
            heappush(self.bigger, -heappushpop(self.smaller, -num))
        else:
            heappush(self.smaller, -heappushpop(self.bigger, num))

    def findMedian(self) -> float:
        
        if len(self.smaller) != len(self.bigger):
            return float(self.bigger[0])
        
        return float(self.bigger[0] - self.smaller[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
