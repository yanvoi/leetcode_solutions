# very inefficient but it's concise and easy to understand
# addNum runs in O(1) and getIntervals in O(n) so on paper it is efficient
class SummaryRanges:

    def __init__(self):
        self.nums = [False] * (10 ** 4)
        

    def addNum(self, value: int) -> None:
        self.nums[value] = True
        

    def getIntervals(self) -> List[List[int]]:
        result = []
        prev = False
        for num, boolean in enumerate(self.nums):
            if boolean and prev:
                result[-1][1] = num
            elif boolean:
                result.append([num, num])
            
            prev = boolean

        return result


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
