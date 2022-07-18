class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 0:
            return 0
        
        max_profit = 0
        min_price = prices[0]
        
        for current in prices[1:]:
            if current < min_price:
                min_price = current
            elif max_profit < current - min_price:
                max_profit = current - min_price
        
        return max_profit
    
