class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        num = ''
        
        negative = False
        if x < 0:
            negative = True
            x = abs(x)
        
        while x > 0:
            num = num + str(x % 10)
            x = x // 10
            
        if negative:
            num = '-' + num
            
        answer = int(num)
        
        if (-1)*(2**31) <= answer <= 2**31 - 1:
            return answer
        else:
            return 0
        
