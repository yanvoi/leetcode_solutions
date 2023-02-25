class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit, min_price = 0, float('inf')
        for price in prices:
            profit = max(profit, price - min_price)
            min_price = min(min_price, price)

        return profit
