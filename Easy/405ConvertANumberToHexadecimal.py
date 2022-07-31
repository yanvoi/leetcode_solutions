class Solution:
    def toHex(self, num: int) -> str:
        
        if num == 0:
            return '0'
        
        hexa = '0123456789abcdef'
        ans = ''
        
        if num < 0:
            num = num + 2**32
        
        while num > 0:
            ans = hexa[(num % 16)] + ans
            num = num // 16
            
        return ans
        
