class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans, minPrice = 0, prices[0]
        
        for price in prices[1:]:
            if price < minPrice:
                minPrice = price
            else:
                ans += price - minPrice
                minPrice = price
        
        return ans
        
