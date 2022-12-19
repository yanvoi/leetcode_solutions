class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) == 1: return 0

        stockPrices.sort(key=lambda x: x[0])
        answer = 1
        for i in range(len(stockPrices) - 2):
            # check if next 3 points are collinear
            if not self.are_collinear(stockPrices[i], stockPrices[i+1], stockPrices[i+2]):
                answer += 1

        return answer


    def are_collinear(self, first: List[int], second: List[int], third: List[int]):
        x1, y1 = first
        x2, y2 = second
        x3, y3 = third

        return (y3 - y2) * (x2 - x1) == (y2 - y1) * (x3 - x2)
