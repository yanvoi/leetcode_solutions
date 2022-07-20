class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        max = 0
        
        for customer in accounts:
            
            customers_wealth = 0
            for i in customer:
                customers_wealth += i
                
            if customers_wealth > max:
                max = customers_wealth
                
        return max
        
