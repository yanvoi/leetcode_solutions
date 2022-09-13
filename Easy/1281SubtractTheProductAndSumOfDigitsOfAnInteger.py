class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        n = str(n)
        
        product, s = 1, 0
        for digit in n:
            product = product * int(digit)
            s += int(digit)
            
        return product - s
        
