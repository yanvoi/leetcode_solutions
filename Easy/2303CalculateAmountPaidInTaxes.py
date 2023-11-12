class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        taxed, prev_upper = 0, 0
        for upper, percent in brackets:
            to_tax = min(upper, income)
            taxed += ((to_tax  - prev_upper) * percent) / 100
            prev_upper = to_tax

        return taxed
